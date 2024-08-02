const express = require('express');
const app = express();

app.use(express.json());

// POST method
app.post('/bfhl', (req, res) => {
    const { email, roll_number, data } = req.body;
    const fullName = "john_doe"; // Replace with actual user full name
    const dob = "17091999"; // Replace with actual date of birth

    const numbers = data.filter(item => !isNaN(item));
    const alphabets = data.filter(item => isNaN(item));

    res.json({
        user_id: `${fullName}_${dob}`,
        is_success: true,
        email,
        roll_number,
        numbers,
        alphabets
    });
});

// GET method
app.get('/bfhl', (req, res) => {
    res.status(200).json({
        operation_code: 1
    });
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
