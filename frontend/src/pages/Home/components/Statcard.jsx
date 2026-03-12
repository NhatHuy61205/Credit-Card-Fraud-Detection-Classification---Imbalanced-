import "./StatCard.css"
import statusConfig from "../../../config/statusConfig";
import React from "react";

export default function StatCard({ status, value }) {

    const config = statusConfig[status]
    return (

        <div
            className="stat-card"
            style={{
                background: config.bg,
                color: config.color
            }}
        >

            <h3>{config.title}</h3>
            <p>{value}</p>

        </div>


    )

}
