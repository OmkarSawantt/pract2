const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const fileUpload = require("express-fileupload");
const path = require("path");
const app = express();
app.use(cors())
app.use(fileUpload());

app.get("/", (req, res) => {
  const fileName = "mainver64bit.txt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);

  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/py", (req, res) => {
  const fileName = "main.py";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);

  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/bfs", (req, res) => {
  const fileName = "bfs.py";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/dfs", (req, res) => {
  const fileName = "bfs.py";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/didfs", (req, res) => {
  const fileName = "didfs.py";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);

  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/nq", (req, res) => {
  const fileName = "nqueen.py";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);

  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/to", (req, res) => {
  const fileName = "towerofhanoi.py";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);

  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/can", (req, res) => {
  const fileName = "misCan.py";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);

  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/nltk", (req, res) => {
  const fileName = "nltkpro.py";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);

  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/the", (req, res) => {
  const fileName = "the.txt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);

  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/aus", (req, res) => {
  const fileName = "aus.txt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);

  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/fam", (req, res) => {
  const fileName = "fam.txt";
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