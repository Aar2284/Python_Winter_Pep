// create a login system as if username is "admin" and password is "password123" print -> "Login successful!" otherwise print -> "Invalid username or password." Otherwise "Invalid credentials"

function login(username, password) {
    if (username === "admin" && password === "password123") {
        console.log("Login successful!");
    } else if (username !== "admin" || password !== "password123") {
        console.log("Invalid username or password.");
    } else {
        console.log("Invalid credentials");
    }
}