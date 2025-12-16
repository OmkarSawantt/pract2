const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const fileUpload = require("express-fileupload");
const path = require("path");
const fs = require('fs');
const app = express();
const archiver = require("archiver");
app.use(cors())
app.use(fileUpload());

app.use("/uploads", express.static(path.join(__dirname, "uploads")));

app.get("/", async(req, res) => {
  const fileName = "wd.txt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/bi1", async(req, res) => {
  const fileName = "Practical1.pbix";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/bi2", async(req, res) => {
  const fileName = "Practical2.pbix";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});



app.get("/2b", async (req, res) => {
  const files = [
    { name: "AdventureWorks2012.bak", path: path.join(__dirname, "uploads/AdventureWorks2012.bak") },
    { name: "AdventureWorksDW2012.bak", path: path.join(__dirname, "uploads/AdventureWorksDW2012.bak") },
  ];

  res.setHeader("Content-Type", "application/zip");
  res.setHeader("Content-Disposition", "attachment; filename=files.zip");

  const archive = archiver("zip", {
    zlib: { level: 9 }, // Maximum compression
  });

  archive.pipe(res);

  // Check if files exist before adding them to the archive
  files.forEach((file) => {
    if (fs.existsSync(file.path)) {
      archive.file(file.path, { name: file.name });
    } else {
      console.error(`File not found: ${file.path}`);
    }
  });

  // Handle errors
  archive.on("error", (err) => {
    console.error("Error creating archive:", err);
    res.status(500).send("Error creating archive");
  });

  // Finalize the archive
  archive.finalize();
});




app.get("/exc", async(req, res) => {
  const fileName = "Excel.xlsx";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/olap", async(req, res) => {
  const fileName = "--DROP DATABASE Sales_DW.txt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/class", async(req, res) => {
  const fileName = "data_classification.R";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/k", async(req, res) => {
  const fileName = "k_means.R";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/lin", async(req, res) => {
  const fileName = "Linear_regression.R";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});

app.get("/log", async (req, res) => {
  const files = [
    { name: "BI_logistic_regression.R", path: path.join(__dirname, "uploads/BI_logistic_regression.R") },
    { name: "quality (2) - quality (2).csv", path: path.join(__dirname, "uploads/quality (2) - quality (2).csv") },
  ];

  res.setHeader("Content-Type", "application/zip");
  res.setHeader("Content-Disposition", "attachment; filename=files.zip");

  const archive = archiver("zip", {
    zlib: { level: 9 },
  });
  archive.pipe(res);
  files.forEach((file) => {
    archive.file(file.path, { name: file.name });
  });
  archive.finalize();
  archive.on("error", (err) => {
    console.error("Error creating archive:", err);
    res.status(500).send("Error creating archive");
  });
});

app.get("/jr", async(req, res) => {
  const fileName = "Journal.pdf";
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
