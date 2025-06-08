import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import './css/AuthForm.css';

const BASE_URL = 'http://localhost:5000';

const AuthForm = () => {
  const [isLogin, setIsLogin] = useState(true);
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const url = `${BASE_URL}${isLogin ? "/auth/login" : "/auth/signup"}`;
    const payload = isLogin
      ? { username, password }
      : { username, email, password };

    try {
      const response = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const data = await response.json();
      if (response.ok) {
        setMessage(data.message || (isLogin ? "Login successful!" : "Signup successful!"));
        if (isLogin) {
          localStorage.setItem("username", username);
          navigate("/dashboard");
        } else {
          setTimeout(() => setIsLogin(true), 1000);
        }
      } else {
        setMessage(data.error || "Something went wrong.");
      }
    } catch (error) {
      console.error("Error:", error);
      setMessage("A network error occurred.");
    }
  };

  return (
    <div className="wrapper">
      <div className="title-text">
        <div className={`title ${isLogin ? "login" : "signup"}`}>
          {isLogin ? "Login Form" : "Signup Form"}
        </div>
      </div>
      <div className="form-container">
        <div className="slide-controls">
          <button
            className={`slide login ${isLogin ? "active" : ""}`}
            onClick={() => setIsLogin(true)}
          >
            Login
          </button>
          <button
            className={`slide signup ${!isLogin ? "active" : ""}`}
            onClick={() => setIsLogin(false)}
          >
            Signup
          </button>
          <div className={`slider-tab ${!isLogin ? "slide-right" : ""}`}></div>
        </div>
        <div className="form-inner">
          <form onSubmit={handleSubmit} className="auth-form">
            {!isLogin && (
              <>
                <div className="field">
                  <input
                    type="email"
                    placeholder="Email Address"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                  />
                </div>
              </>
            )}
            <div className="field">
              <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>
            <div className="field">
              <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            <div className="field btn">
              <div className="btn-layer"></div>
              <input type="submit" value={isLogin ? "Login" : "Signup"} />
            </div>
            <div className="signup-link">
              {isLogin ? (
                <>
                  Don't have an account? <span onClick={() => setIsLogin(false)}>Signup now</span>
                </>
              ) : (
                <>
                  Already have an account? <span onClick={() => setIsLogin(true)}>Login</span>
                </>
              )}
            </div>
            {message && <p className="status-msg">{message}</p>}
          </form>
        </div>
      </div>
    </div>
  );
};

export default AuthForm;
