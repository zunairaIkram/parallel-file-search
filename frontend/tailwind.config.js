import flowbite from "flowbite-react/tailwind";

/** @type {import('tailwindcss').Config} */
export default {
	content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}", flowbite.content()],
	theme: {
		extend: {
			boxShadow: {
				whiteLg:
					"0 10px 15px rgba(255, 255, 255, 0.1), 0 4px 6px rgba(255, 255, 255, 0.05)",
			},
		},
	},
	plugins: [flowbite.plugin()],
};
