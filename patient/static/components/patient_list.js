const patientList = async () => {
  const patient_list_patient_section = document.getElementById(
    "patient-list-patient-section"
  );
  const url = "/patient/patient-list/";
  try {
    const res = await fetch(url);
    if (!res.ok) {
      throw new Error("Response was not ok!");
    }
    const data = await res.json();
    const patients = data.data;
    console.log("patient", patients);
    patient_list_patient_section.innerHTML = "";
    patients.forEach((patient) => {
      patient_list_patient_section.innerHTML += `<div class="row">
          <div class="col-lg-2 border-bottom py-3 name">
          <img class='rounded-circle border me-1' style='width:25px; height:25px; object-fit:cover' src ='${patient.avatar}' alt='avatar'> 
          <span class='patient-name'>${patient.name} </span>  
          </div>
          <div class="col-lg-3 border-bottom py-3 email">
          <i style="color:var(--primary-color)" class="fa-solid fa-envelope me-2"></i>
          <span class='patient-email'>${patient.email} </span>
          </div>
          <div class="col-lg-2 border-bottom py-3 phone">
          <i style="color:var(--primary-color)" class="fa-solid fa-phone me-2"></i>
          <span class='patient-phone'> + ${patient.phone} </span>
          </div>
          <div class="col-lg-1 border-bottom py-3 age"><span class='patient-age'>${patient.age}</span></div>
          <div class="col-lg-2 border-bottom  py-3 gender"><span class='patient-gender'>${patient.gender}</span> </div>
          <div class="col-lg-2 border-bottom py-3 blood_group"><span class='patient-blood-group'>${patient.blood_group}</span></div>
          </div>`;
    });
  } catch (error) {
    console.log("error", error);
  }
};

patientList();
