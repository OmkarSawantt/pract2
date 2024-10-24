const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const fileUpload = require("express-fileupload");
const path = require("path");
const app = express();
app.use(cors())
app.use(fileUpload());

app.get("/", (req, res) => {
  const fileName = "userss.txt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);

  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/1", (req, res) => {
  const fileName = "main64bit2.txt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);

  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/z", (req, res) => {
  const fileName = "0All.zip";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);

  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/z2", (req, res) => {
  const fileName = "0All2.zip";
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