import React from "react"
import "./Home.css"
import StatCard from "./Components/Statcard"
import Segment from "./Components/Segment"

export default function Home() {
  const stats = [
    { status: "disputed", value: 0 },
    { status: "early", value: 0 },
    { status: "refunded", value: "0%" },
    { status: "success", value: 0 },
    { status: "failed", value: 0 }
  ]

  const segments = [

    { bg: "#f5b041", width: "3%" },
    { bg: "#ff7f0e", width: "2%" },
    { bg: "#6c5ce7", width: "4%" },
    { bg: "#2e86de", width: "70%" },
    { bg: "#00bcd4", width: "21%" }

  ]
  return (
    <section className="home-container">

      <div className="fraud-status">

        <h2>Rules performance</h2>
        <span className="line"></span>
        <div className="total-payments">
          0 Matching payments
          <div className="time">
            in the last 24 hours
          </div>
        </div>
        <div className="stats-container">

          {
            stats.map((item, index) => (<StatCard
                key={index}
                status={item.status}
                value={item.value}/>))
          }

        </div>
        <div className="rule-bar">

          {
            segments.map((seg, index) => (<Segment 
                key={index}
                bg={seg.bg}
                width={seg.width}/>))
          }

        </div>
      </div>

    </section>
  );
}