import React, { useEffect, useState } from 'react';
import '../css/Dashboard.css'; 
import NavBar from '../components/NavBar';

const BASE_URL = 'http://localhost:5000';

const Dashboard = () => {
  const [username, setUsername] = useState(''); 
  const [groups, setGroups] = useState([]);
  const [userBalances, setUserBalances] = useState([]);

  useEffect(() => {
     const savedUsername = localStorage.getItem("username");
     if (savedUsername) {
      setUsername(savedUsername);
  }

  const fetchData = async () => {
    try{
      const response = await fetch(`${BASE_URL}/groups/`);
      const groupData = await response.json();
      setGroups(groupData);

      const balances = await Promise.all(groupData.map(group =>
        fetch(`${BASE_URL}/transactions/balance/${savedUsername}/${group.group_id}`)
          .then(res => res.json())
      ));
      setUserBalances(balances);
    } catch (error) {
      console.error('Error fetching groups:', error);
    }
  }
  fetchData();
  }, []);

  return (
      <div className="main-content">
        <h1>Karibu, {username}</h1>
      
        <div className="cards">
          {userBalances.map((balance, idx) => (
            <div className="card balance-card" key={idx}>
              <h3>Total Balance</h3>
              <p className="amount">Ksh {Number(balance).toFixed(2)}</p>
              <p>{balance.message}</p>
              <p><strong>Group:</strong> {balance.group}</p>
            </div>
          ))}
          <div className="card groups-card">
            <h3>Your Groups</h3>
            <ul>
              {groups.length > 0 ? (
                groups.map(group => (
                  <li key={group.group_id}>{group.group_name}</li>
                ))
              ) : (
                <li>No groups found</li>
              )}
            </ul>
          </div>
        </div>

        <div className="transactions">
          <h3>Recent Transactions</h3>
        </div>
      </div>
   
  );
};

export default Dashboard;
