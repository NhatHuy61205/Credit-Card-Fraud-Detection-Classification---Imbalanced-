import React from "react";
import { useEffect, useState } from "react";
import "./Payments.css"
import StatCard from "./statcard/Statcard"
import Segment from "./segment/Segment"
import PaymentsBarChart from "./barchart/PaymentsBarChart";
import Table from "./table/Table";

export default function Payments() {
  const [status, setStatus] = useState("");
  const [total, setTotal] = useState(0);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/data/total")
      .then(res => res.json())
      .then(data => setTotal(data))
      .catch(err => console.error(err));
  }, []);

  const [stat, setStat] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/data/amount-per-status")
      .then(res => res.json())
      .then(data => setStat(data))
      .catch(err => console.error(err));
  }, []);


  return (
    <section className="home-container">

      <div className="fraud-status">

        <h2>Rules performance</h2>
        <span className="line"></span>
        <div className="total-payments">
          <p>{total.toLocaleString("en-US")} Matching payments</p>
          <div className="calendar-btn">
            <i className="fa-regular fa-calendar-days"></i>
            <p>0/0/0 - 0/0/0</p>
          </div>
        </div>
        <div className="stats-container">

          {stat.map((item, index) => (
            <StatCard
              key={index}
              status={item.status}
              value={Number(item.Amount).toLocaleString("en-US")}
            />
          ))}

        </div>
        <div className="rule-bar">

          {stat.map((item, index) => (
            <Segment
              key={index}
              bg={item.bg}
              width={item.percent + "%"}
            />
          ))}

        </div>
      </div>

      <div className="payments-chart">
        <PaymentsBarChart />
      </div>
      <div className="payments-dataframe">
        <h3>Payments</h3>
        <select value={status} onChange={(e) => setStatus(e.target.value)}>
          <option value="">-- Chọn trạng thái --</option>
          <option value="Success">success</option>
          <option value="Disputed">disputed</option>
          <option value="Warning">Warning</option>
        </select>
        <Table status = {status} />
      </div>
    </section>
  );
}