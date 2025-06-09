import React, { useEffect, useState } from 'react';
import GroupDetails from './GroupDetails';
import '../css/Group.css';

const BASE_URL = 'http://localhost:5000';

function Groups() {
  const [groups, setGroups] = useState([]);
  const [selectedGroup, setSelectedGroup] = useState(null);
  const [name, setName] = useState('');
  const [desc, setDesc] = useState('');

  useEffect(() => {
    fetch(`${BASE_URL}/groups/`)
      .then(res => res.json())
      .then(setGroups);
  }, []);

  const createGroup = () => {
    fetch(`${BASE_URL}/groups/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, description: desc })
    })
      .then(res => res.json())
      .then(data => {
        setGroups([...groups, data]);
        setName('');
        setDesc('');
      });
  };

  const deleteGroup = (id) => {
    fetch(`${BASE_URL}/groups/${id}`, { method: 'DELETE' })
      .then(() => {
        setGroups(groups.filter(g => g.group_id !== id));
        if (selectedGroup?.group_id === id) setSelectedGroup(null);
      });
  };

  return (
    <div className="groups-page">
      <h2>Groups</h2>
      <div className="group-form">
        <input placeholder="Name" value={name} onChange={e => setName(e.target.value)} />
        <input placeholder="Description" value={desc} onChange={e => setDesc(e.target.value)} />
        <button onClick={createGroup}>Create</button>
      </div>
      <ul className="group-list">
        {groups.map(g => (
          <li key={g.group_id} className="group-item">
            <div><strong>{g.group_name}</strong> – {g.description}</div>
            <div>
              <button onClick={() => setSelectedGroup(g)}>View</button>
              <button onClick={() => deleteGroup(g.group_id)}>Delete</button>
            </div>
          </li>
        ))}
      </ul>
      {selectedGroup && <GroupDetails group={selectedGroup} />}
    </div>
  );
}

export default Groups;
