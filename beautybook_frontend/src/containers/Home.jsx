import React from 'react'
import { Logout } from '../components';
import axios from "axios";

const Home = () => {

    const user_name= localStorage.getItem('username');
    const a_token = localStorage.getItem('access_token');
    const r_token = localStorage.getItem('refresh_token');
    return (
        <div>
            <div> username : {user_name} </div>
            <div> a_token : {a_token} </div>
            <div> t_token : {r_token} </div>

            
            
            <div className='flex justify-center'>
              <Logout />
            </div>
        </div>

    )
}

export default Home
