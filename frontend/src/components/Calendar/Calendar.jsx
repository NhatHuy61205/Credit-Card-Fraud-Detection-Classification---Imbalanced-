import { useState } from "react"
import "./Calendar.css"

export default function Calendar() {

  const months = [
    'THÁNG MỘT','THÁNG HAI','THÁNG BA','THÁNG TƯ','THÁNG NĂM',
    'THÁNG SÁU','THÁNG BẢY','THÁNG TÁM','THÁNG CHÍN',
    'THÁNG MƯỜI','THÁNG MƯỜI MỘT','THÁNG MƯỜI HAI'
  ]

  const [date] = useState(new Date())
  const [goDate,setGoDate] = useState(null)
  const [backDate,setBackDate] = useState(null)
  const [hoverDay,setHoverDay] = useState(null)

  const y = date.getFullYear()
  const m = date.getMonth()

  const renderDays = () => {

    const firstDay = new Date(y, m, 1)
    const lastDay = new Date(y, m + 1, 0)

    const days = lastDay.getDate()

    const startDay = firstDay.getDay() === 0 ? 7 : firstDay.getDay()

    const arr = []

    for(let i=1;i<startDay;i++){
      arr.push(null)
    }

    for(let i=1;i<=days;i++){
      arr.push(i)
    }

    return arr
  }

  const days = renderDays()

  function handleClick(day){

    if(!goDate){
      setGoDate(day)
      return
    }

    if(!backDate){
      if(day < goDate){
        setBackDate(goDate)
        setGoDate(day)
      }else{
        setBackDate(day)
      }
      return
    }

    setGoDate(day)
    setBackDate(null)
  }

  function getClass(day){

    if(!day) return ""

    let cls = "day"

    if(goDate === day) cls += " Di"

    if(backDate === day) cls += " Ve"

    if(goDate && !backDate && hoverDay){

      if(
        (day > goDate && day < hoverDay) ||
        (day < goDate && day > hoverDay)
      ){
        cls += " gap"
      }
    }

    return cls
  }

  return (
    <div className="calendar">

      <h3>{months[m]} {y}</h3>

      <table>

        <tbody>

          {Array.from({length: Math.ceil(days.length/7)}).map((_,row)=>{

            return(
              <tr key={row}>

                {days.slice(row*7,row*7+7).map((day,i)=>(
                  <td
                    key={i}
                    className={getClass(day)}
                    onClick={()=>day && handleClick(day)}
                    onMouseOver={()=>setHoverDay(day)}
                  >
                    {day}
                  </td>
                ))}

              </tr>
            )

          })}

        </tbody>

      </table>

    </div>
  )
}

