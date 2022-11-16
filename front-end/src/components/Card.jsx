import React, { useState } from "react";
import Select from "react-select";

function Card() {
  const [roomSelected, setroomSelected] = useState(null);
  const [genderSelected, setgenderSelected] = useState(null);
  let [text, setText] = useState(null);
  const roomType = [
    { value: "พัดลม", label: "พัดลม" },
    { value: "แอร์", label: "แอร์" },
    { value: "สูท", label: "สูท" },
  ];
  let gender = [
    { value: "ชาย", label: "ชาย" },
    { value: "หญิง", label: "หญิง" },
    { value: "รวม", label: "รวม" },
  ];

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(
      event.target[2].value,
      roomSelected.value,
      genderSelected.value
    );
  };

  const RoomSelectComponent = (options) => {
    return (
      <div className="select">
        <Select
          value={roomSelected}
          onChange={setroomSelected}
          options={options}
        />
      </div>
    );
  };
  const GenderSelectComponent = (options) => {
    return (
      <div className="select">
        <Select
          value={genderSelected}
          onChange={setgenderSelected}
          options={options}
        />
      </div>
    );
  };

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
        <label>ประเภทหอ{GenderSelectComponent(gender)}</label>
        <label>ประเภทห้อง{RoomSelectComponent(roomType)}</label>
        <label>
          price <br/>
          <input type="text" name="price" />
        </label>
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
}

export default Card;
