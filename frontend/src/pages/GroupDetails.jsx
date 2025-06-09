import React, { useEffect, useState } from 'react';
import '../css/Group.css';

const BASE_URL = 'http://localhost:5000';

function GroupDetails({ group }) {
  const [members, setMembers] = useState([]);
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    if (!group) return;

    fetch(`${BASE_URL}/group-members/${group.group_name}`)
      .then(res => res.json())
      .then(data => {
        setMembers(data);
        return Promise.all(
          data.map(m =>
            fetch(`${BASE_URL}/transactions/${m.user.username}/${group.group_name}`)
              .then(res => res.json())
              .then(tx => ({ username: m.user.username, tx }))
          )
        );
      })
      .then(setTransactions)
      .catch(err => console.error('Error loading group details', err));
  }, [group]);

  return (
    <div className="group-details">
      <h3>Members of {group.group_name}</h3>
      <ul className="member-list">
        {members.map(m => (
          <li key={m.id}>
            <strong>{m.user.username}</strong> – {m.role} (joined {new Date(m.joined_at).toLocaleDateString()})
          </li>
        ))}
      </ul>

      <h3>Transactions</h3>
      {transactions.map(user => (
        <div key={user.username}>
          <h4>{user.username}</h4>
          <ul className="tx-list">
            {Array.isArray(user.tx) ? user.tx.map(t => (
              <li key={t.id}>
                {t.transaction_type}: Ksh {t.amount} on {new Date(t.timestamp).toLocaleDateString()}
              </li>
            )) : <li>No transactions</li>}
          </ul>
        </div>
      ))}
    </div>
  );
}

export default GroupDetails;
