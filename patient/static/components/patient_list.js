const patientList = async () => {
  const patient_list = document.getElementById("patient-list-patient-section");
  const url = "/patient/patient-list/";
  try {
    const res = await fetch(url);
    if (!res.ok) {
      throw new Error("Response was not ok!");
    }
    const data = await res.json();
    const patients = data.data;
    console.log("patient", patients);
    patient_list.innerHTML = "";
    patients.forEach((patient) => {
      patient_list.innerHTML += `<div class="row">
          <div class="col-lg-2 name">${patient.name}</div>
          <div class="col-lg-1 age">${patient.age}</div>
          <div class="col-lg-2 gender">${patient.gender} </div>
          <div class="col-lg-2 blood_group">${patient.blood_group}</div>
          <div class="col-lg-2 phone">${patient.phone}</div>
          <div class="col-lg-3 email">${patient.email}</div>
        </div>`;
    });
  } catch (error) {
    console.log("error", error);
  }
};

patientList();
