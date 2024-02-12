import React from "react";

const Logout = () => {
  const logout = async () => {
    try {
      const bearer_token = localStorage.getItem('access_token')
      const bearer = 'Bearer ' + bearer_token;
      const apiURL = 'http://localhost:8000/auth/logout/'
      let opts = {
        "refresh" : localStorage.getItem('refresh_token')
      }
      
      const response = await fetch(apiURL, {
          method: 'POST',
          withCredentials: true,
          headers: {
              'Content-Type': 'application/json',
              'Authorization': bearer, 
          },
          body: JSON.stringify(opts)
      })
      console.log("success fully logged out")
      console.log(response)

      localStorage.clear();
      
      window.location.href = '/login'
    } catch (e) {
      console.log("logout not working", e);
    }
  };

  return (
    <div>
      <button
        type="submit"
        className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
        onClick={logout}
      >
        Log out
      </button>
    </div>
  );
};

export default Logout;
