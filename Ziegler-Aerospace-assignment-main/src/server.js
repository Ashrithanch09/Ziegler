const express = require("express");
const dotenv = require("dotenv");
const cors = require("cors");
const { userRouter } = require("../Routes/userRouter");
require("../db/connection");
dotenv.config();

const app = express();
app.use(express.json());
app.use(cors());

const PORT = 5500;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});


app.use("/api/users", userRouter);

app.listen(PORT, () => {
  console.log(`server running at port: ${PORT}`);
});
