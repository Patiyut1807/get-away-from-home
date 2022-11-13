import React, { useState } from "react";
import Select from 'react-select';


const optionSS = [
    { value: 'chocolate', label: 'Chocolate' },
    { value: 'strawberry', label: 'Strawberry' },
    { value: 'vanilla', label: 'Vanilla' },
  ];
  
  const SelectComponent=(options)=> {
    const [selectedOption, setSelectedOption] = useState(null);
  
    return (
      <div className="select">
        <Select
          value={selectedOption}
          onChange={setSelectedOption}
          options={options}
        />
      </div>
    );
  }




function Card() {
  let [text, setText] = useState(null);
  let roomType = ["พัดลม", "แอร์", "สูท"];
  let gender = ["ชาย", "หญิง", "รวม"];

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(event);
  }
  return (
    <div
      className="card"
      style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        width: "60%",
        height: "75%",
        boxSizing: "border-box",
        border: "5px solid #7DEAE7",
        borderRadius: "15px",
      }}
    >
      <form onSubmit={handleSubmit}>
        <label>
            {SelectComponent(optionSS)}
          Name:
          <input type="text" name="name" />
        </label>
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
}

export default Card;
