import React from 'react'
import axios from "axios";
import {useState} from "react";
import { Link } from 'react-router-dom';

const Signin = () => {
  const [username, setUsername] = useState('');
  const [Email, setEmail] = useState('');
  const [phone_number, setphone_number] = useState('');
  const [password, setPassword] = useState('');

  const submit = async (e)=>{
    e.preventDefault();
    const user= {
      username: username,
      email: Email,
      phone_number: phone_number,
      password: password
    }

    try {
      const {data} = await axios.post('http://localhost:8000/auth/register/', 
                                    user,
                                    {headers: {'Content-Type': 'application/json'},
                                    withCredentials: false});
      console.log(data);
      window.location.href = '/login'
    } catch (err) {
      if (err.response?.status === 400) {
        console.log(err.response.data)
    }
    }


    
  }

  return (
    <>
      <div className="flex min-h-full flex-col justify-center py-12 lg:px-5 ">

        <div className="sm:mx-auto sm:w-full sm:max-w-sm">
          {/* <img
            className="mx-auto h-10 w-auto"
            src=""
            alt="Your Company"
          /> */}
          <h2 className="py-2 text-center text-2xl font-bold leading-9 text-gray-900">
            Lets, Get Started!!
          </h2>
          <h2 className="py-2 mt-2 text-center text-2l font-light leading-9 tracking-tight text-gray-500">
            Create your Account
          </h2>
        </div>
        
        <div className="pl-3 mt-1 sm:mx-auto sm:w-full sm:max-w-sm">
          <form className="space-y-6" onSubmit={submit}>
            <div>
              <label htmlFor="email" className="block text-sm font-medium leading-6 text-gray-900">
                Email address
              </label>
              <div className="mt-2">
                <input
                  name="Email"
                  type="text"
                  required
                  placeholder="Enter your Email Address"
                  className="pl-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  onChange={e => setEmail(e.target.value)}
                />
              </div>
            </div>
            <div>
              <label htmlFor="username" className="block text-sm font-medium leading-6 text-gray-900">
                Username
              </label>
              <div className="mt-2">
                <input
                  name="username"
                  type="text"
                  required
                  placeholder="Enter your Name"
                  className="pl-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  onChange={e => setUsername(e.target.value)}
                />
              </div>
            </div>
            <div>
              <div className='flex space-x-2.5'>
              <label htmlFor="phone_number" className="block text-sm font-medium leading-6 text-gray-900">
                Phone Number 
              </label>
              <div className='block text-xs leading-6 text-gray-400'>(+91)</div>
              </div>
              <div className="mt-2">
                <input
                  name="contact"
                  type="text"
                  required
                  placeholder="Enter your Phone Number"
                  className="pl-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                  onChange={e => setphone_number(e.target.value)}
                />
              </div>
            </div>
            <div>
              <div className="flex items-center justify-between">
                <label htmlFor="password" className="block text-sm font-medium leading-6 text-gray-900">
                  Password
                </label>
              </div>
              <div className="mt-2">
                <input
                  id="password"
                  name="password"
                  type="password"
                  autoComplete="current-password"
                  placeholder="Enter your Password"
                  required
                  className="pl-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 "
                  onChange={e => setPassword(e.target.value)}
                />
              </div>
            </div>

            <div>
              <button
                type="submit"
                className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              >
                Create Your Account!
              </button>
            </div>
          </form>
          <div className="flex items-center justify-center py-2">
            <div className="text-sm italic font-serif text-gray-500">
              Got an Account ?, 
            </div>
            <div className="pl-2 text-sm">
              <Link to="/login" className="font-semibold text-indigo-400 hover:text-indigo-600">
                Log In
              </Link>
            </div>
          </div>
      </div>
      </div>
    </>
  )
}

export default Signin
