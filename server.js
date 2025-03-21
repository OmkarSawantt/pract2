const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const fileUpload = require("express-fileupload");
const path = require("path");
const app = express();
app.use(cors())
app.use(fileUpload());

app.get("/acn", async(req, res) => {
  const fileName = "ACN.txt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get("/", async(req, res) => {
  const fileName = "ACN.txt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});

app.get("/acn/java", async (req, res) => {
  const fileName2 = "ACN1.txt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath2 = path.join(directoryPath, fileName2);

  res.download(filePath2, fileName2, (err) => {
    if (err) {
      console.log("Error downloading file2:", err);
      res.status(500).send("Error downloading file2.");
    }
  });
})

app.get("/acn/java1", async (req, res) => {
  const fileName2 = "java1.zip";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath2 = path.join(directoryPath, fileName2);

  res.download(filePath2, fileName2, (err) => {
    if (err) {
      console.log("Error downloading file2:", err);
      res.status(500).send("Error downloading file2.");
    }
  });
});
app.get("/acn/java2", async (req, res) => {
  const fileName2 = "java2.zip";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath2 = path.join(directoryPath, fileName2);

  res.download(filePath2, fileName2, (err) => {
    if (err) {
      console.log("Error downloading file2:", err);
      res.status(500).send("Error downloading file2.");
    }
  });
});

app.get('/acn/rip', async(req, res) => {
  const fileName = "RIP.pkt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get('/acn/ospf', async(req, res) => {
  const fileName = "OSPF.pkt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get('/acn/bgp', async(req, res) => {
  const fileName = "BGP.pkt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get('/acn/acl', async(req, res) => {
  const fileName = "ACL.pkt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get('/acn/dd', async(req, res) => {
  const fileName = "DHCP_DNS.pkt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get('/acn/email', async(req, res) => {
  const fileName = "SMTP_POP3.pkt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get('/acn/tel', async(req, res) => {
  const fileName = "Telnet.pkt";
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
