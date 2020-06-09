import React from 'react';
import { useTheme } from '@material-ui/core/styles';
import { BarChart, Bar, XAxis, YAxis, Label, ResponsiveContainer } from 'recharts';
import Title from './Title';

// Generate Sales Data
function createData(game, cspm) {
  return { game, cspm };
}

const data = [
  createData('0', 4.1),
  createData('1', 1.9),
  createData('2', 4.2),
  createData('3', 2.2),
  createData('4', 4.3),
  createData('5', 7.5),
  createData('6', 7.4),
  createData('7', 6.1),
  createData('8', 2.5),
  createData('9', 0.2),
  createData('10', 4.1),
  createData('11', 2.4),
  createData('12', 1.8),
  createData('13', 5.9),
  createData('14', 1.6),
  createData('15', 6.7),
  createData('16', 6.9),
  createData('17', 6.8),
  createData('18', 6.8),
  createData('19', 7.5),
  createData('20', 6.3),
  createData('21', 7.9),
  createData('22', 6.3),
  createData('23', 4.1),
  createData('24', 6.8),
  createData('25', 4),
  createData('26', .9),
  createData('27', 4),
  createData('28', .9),
  createData('29', 3.1),
  createData('30', undefined),
];

export default function Chart() {
  const theme = useTheme();

  return (
    <React.Fragment>
      <Title>CS/Min Over 30 Games</Title>
      <ResponsiveContainer>
        <BarChart
          data={data}
          margin={{
            top: 16,
            right: 16,
            bottom: 0,
            left: 24,
          }}
        >
          <XAxis dataKey="game" stroke={theme.palette.text.secondary} />
          <YAxis stroke={theme.palette.text.secondary}>
            <Label
              angle={270}
              position="left"
              style={{ textAnchor: 'middle', fill: theme.palette.text.primary }}
            >
              CS/Min 
            </Label>
          </YAxis>
          <Bar dataKey="cspm" fill="#8884d8" />
        </BarChart>
      </ResponsiveContainer>
    </React.Fragment>
  );
}
