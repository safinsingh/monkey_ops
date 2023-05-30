import React from "react";

const Nav = () => {
	return (
		<div className="w-full flex flex-row justify-between content-center bg-cyan-600 h-20 text-white">
			<h1 className="mx-6 font-extrabold my-auto text-2xl underline">
				<span>monkey_ops</span>
			</h1>
			<h2 className="text-center mx-6 font-bold text-xl my-auto ">
				<span>
					<a href="">log in</a>
				</span>
			</h2>
		</div>
	);
};

export default Nav;
