const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const fileUpload = require("express-fileupload");
const path = require("path");
const app = express();
app.use(cors())
app.use(fileUpload());

app.get("/", async(req, res) => {
  res.redirect('https://firebasestorage.googleapis.com/v0/b/uploadingfile-1f51f.appspot.com/o/pract%2FdirectX.zip?alt=media&token=6d84c35d-9756-4cba-8e41-0ef883752241');
});
app.get("/uf", (req, res) => {
  res.redirect('https://firebasestorage.googleapis.com/v0/b/uploadingfile-1f51f.appspot.com/o/pract%2F2Dufo.zip?alt=media&token=facea819-dd39-4efb-8982-a92fa05f88a3');
});
app.get("/rb", (req, res) => {
  res.redirect('https://firebasestorage.googleapis.com/v0/b/uploadingfile-1f51f.appspot.com/o/pract%2FRoll-a-Ball-main.zip?alt=media&token=f7104989-2107-4152-be08-5a83994ab918');
});
app.get("/ss", (req, res) => {
  const fileName = "unity-space-shooter-master.zip";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/rb2", (req, res) => {
  const fileName = "Unity-Roll-a-Ball-main.zip";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});

app.listen(4000, () => {
  console.log(`Server Running On 4000`);
});
