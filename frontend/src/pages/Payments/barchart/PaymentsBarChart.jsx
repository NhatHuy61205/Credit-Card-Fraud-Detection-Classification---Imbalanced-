import React, { useEffect, useState } from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const PaymentsBarChart = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/data/amount-per-hour")
      .then(res => res.json())
      .then(data => setData(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div style={{ width: "100%", height: 400 }}>
      <ResponsiveContainer width="100%" height={400}>
        <BarChart data={data} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
          <XAxis dataKey="Hour_from_start_mod24" label={{ value: "Hour", position: "insideBottomRight", offset: -5 }} />
          <YAxis />
          <Tooltip />
          <Bar dataKey="success" stackId="a" fill="#2e86de" />
          <Bar dataKey="disputed" stackId="a" fill="#f5b041" />
          <Bar dataKey="early" stackId="a" fill="#ff7f0e" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default PaymentsBarChart;