const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const fileUpload = require("express-fileupload");
const path = require("path");
const fs = require('fs');
const app = express();
app.use(cors())
app.use(fileUpload());

app.get("/cc", async(req, res) => {
  const fileName = "Cloud.txt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});
app.get('/jr', async (req, res) => {
  const fileName = 'journal.pdf';
  const directoryPath = path.join(__dirname, 'uploads');
  const filePath = path.join(directoryPath, fileName);

  // Check if the file exists before attempting to download
  if (fs.existsSync(filePath)) {
    // Set correct MIME type for .docx
    res.setHeader(
      'Content-Type',
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    );
    res.setHeader(
      'Content-Disposition',
      `attachment; filename="${fileName}"`
    );

    // Use res.sendFile as fallback for res.download if needed
    res.download(filePath, fileName, (err) => {
      if (err) {
        console.error('Error downloading file:', err);

        // Fallback to res.sendFile if res.download fails
        res.sendFile(filePath, (err2) => {
          if (err2) {
            console.error('Error sending file:', err2);
            res.status(500).send('File could not be downloaded.');
          }
        });
      }
    });
  } else {
    console.error('File not found:', filePath);
    res.status(404).send('File not found.');
  }
});
app.get("/", async(req, res) => {
  const fileName = "Cloud.txt";
  const directoryPath = path.join(__dirname, "uploads");
  const filePath = path.join(directoryPath, fileName);
  res.download(filePath, fileName, (err) => {
    if (err) {
      console.log("Error downloading file:", err);
      res.status(500).send("File could not be downloaded.");
    }
  });
});


app.get("/me", async(req, res) => {
  res.redirect('https://rb.gy/chd0oo');
});



app.listen(4000, () => {
  console.log(`Server Running On 4000`);
});
