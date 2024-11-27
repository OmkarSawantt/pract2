const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const fileUpload = require("express-fileupload");
const path = require("path");
const app = express();
app.use(cors())
app.use(fileUpload());

app.get("/", async(req, res) => {
  res.redirect('https://firebasestorage.googleapis.com/v0/b/uploadingfile-1f51f.appspot.com/o/pract%2FAll.py?alt=media&token=e11c0c61-6f5d-4e1e-a120-38e6566916df');
});
app.get("/cc", async(req, res) => {
  res.redirect('https://firebasestorage.googleapis.com/v0/b/uploadingfile-1f51f.appspot.com/o/pract%2Fall%2FCeaserCipher.py?alt=media&token=cb3c8a3d-f0a9-453b-9d16-bfb755e309c6');
});
app.get("/pf", async(req, res) => {
  res.redirect('https://firebasestorage.googleapis.com/v0/b/uploadingfile-1f51f.appspot.com/o/pract%2Fall%2FPlayFair.py?alt=media&token=0925b234-a4cf-4142-9aea-f64de6c9fa66');
});
app.get("/rsa", async(req, res) => {
  res.redirect('https://firebasestorage.googleapis.com/v0/b/uploadingfile-1f51f.appspot.com/o/pract%2Fall%2FRSA.py?alt=media&token=998a6c1c-c8bc-4057-a206-0e8b01a4117f');
});
app.get("/v", async(req, res) => {
  res.redirect('https://firebasestorage.googleapis.com/v0/b/uploadingfile-1f51f.appspot.com/o/pract%2Fall%2FVernam.py?alt=media&token=2b0b960d-dbaf-410e-b35f-571979d4794d');
});
app.get("/ct", async(req, res) => {
  res.redirect('https://firebasestorage.googleapis.com/v0/b/uploadingfile-1f51f.appspot.com/o/pract%2Fall%2Fcolumnartransposition.py?alt=media&token=046d33b5-568a-46ca-a9df-f3df9c86657d');
});
app.get("/ma", async(req, res) => {
  res.redirect('https://firebasestorage.googleapis.com/v0/b/uploadingfile-1f51f.appspot.com/o/pract%2Fall%2Fmonoalphabetic.py?alt=media&token=8e2355d5-e191-412f-8eb9-6b239252457d');
});
app.get("/pa", async(req, res) => {
  res.redirect('https://firebasestorage.googleapis.com/v0/b/uploadingfile-1f51f.appspot.com/o/pract%2Fall%2Fpolyalphabeticcipher.py?alt=media&token=39451ed2-684b-4c44-a1e7-50e4902e85ee');
});
app.get("/rf", async(req, res) => {
  res.redirect('https://firebasestorage.googleapis.com/v0/b/uploadingfile-1f51f.appspot.com/o/pract%2Fall%2Fraifence.py?alt=media&token=cc51140d-020b-4977-9d7b-af25c49dbe3b');
});



app.listen(4000, () => {
  console.log(`Server Running On 4000`);
});
