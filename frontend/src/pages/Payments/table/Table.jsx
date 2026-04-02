import React, { useEffect, useState } from "react";
import "./Table.css"

export default function Table({ status }) {
    const [stat, setStat] = useState([]);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/?skip=0&limit=20&status=${status}`)
            .then(res => res.json())
            .then(data => setStat(data))
            .catch(err => console.error(err));
    }, [status]);

    const statusStyle = {
        success: { color: "#0984e3" },
        disputed: { color: "#e67e22" },
        warning: { color: "#d63031" }
    };
    return (
        <div style={{ padding: 20 }}>

            <table className="payments-table">
                <thead>
                    <tr>
                        <th>Amount</th>
                        <th>Description</th>
                        <th>Customer</th>
                        <th>Time</th>
                    </tr>
                </thead>

                <tbody>
                    {stat.map((item, index) => (
                        <tr key={index}>
                            <td>
                                <div className="amount-cell">
                                    <div>
                                        <i className="fa-solid fa-dollar-sign"></i>  <span>{Number(item.Amount).toLocaleString("en-US")} USD</span>
                                    </div>

                                    <span style={statusStyle[item.status]}>{item.status}</span>
                                </div>
                            </td>
                            <td>{item.V1}</td>
                            <td>{item.V28}</td>
                            <td>{item.Time}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}