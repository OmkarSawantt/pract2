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



app.listen(4000, () => {
  console.log(`Server Running On 4000`);
});
