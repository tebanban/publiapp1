const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			message: null,
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			],

			site: [
				{
					code: "SJ36-A",
					title: "Rotonda Garantías Sociales",
					owner: "Corporación Rimark R y M S.A.",
					contact: "Virginia Matamoros Mesén",
					phone: "506 2224 5262",
					address: "Zapote",
					background: "white",
					initial: "white"
				},
				{
					code: "SJ36-C",
					title: "Rotonda Garantías Sociales",
					owner: "Corporación Rimark R y M S.A.",
					contact: "Virginia Matamoros Mesén",
					phone: "506 2224 5262",
					address: "Zapote",
					background: "white",
					initial: "white"
				},
				{
					code: "SJ37-A",
					title: "Canal 7 costado sur",
					owner: "Marche Internacional ",
					contact: "José Luis Cavallini Sandoval",
					phone: "506 5555 5555",
					address: "La Sabana",
					background: "white",
					initial: "white"
				},
				{
					code: "SJ37-C",
					title: "Canal 7 costado sur",
					owner: "Marche Internacional ",
					contact: "José Luis Cavallini Sandoval",
					phone: "506 5555 5555",
					address: "La Sabana",
					background: "white",
					initial: "white"
				},
				{
					code: "AL10-A ",
					owner: "IGNACIO MENDEZ RODRIGUEZ",
					size: "12.60 X 5.00 ",
					type: "Unipolar 2 Caras",
					price: "900.00",
					pricelow: "900.00",
					way: "SAN JOSE - CALDERA ",
					title: "AUTOPISTA GENERAL CAÑAS ",
					orientation: "Horizontal ",
					client: "GEOVANNI ",
					state: "Reservada",
					registred: "5/7/19",
					user: "oguzman"
				},
				{
					code: "AL10-C ",
					owner: "IGNACIO MENDEZ RODRIGUEZ",
					size: "12.50 X 5.00 ",
					type: "Unipolar 2 Caras",
					price: "950.00",
					pricelow: "950.00",
					way: "CALDERA - SAN JOSE ",
					title: "AUTOPISTA GENERAL CAÑAS",
					orientation: "Horizontal ",
					client: "NO HAY CLIENTE ACTUAL",
					state: "Disponible ",
					registred: "8/30/18",
					user: "oguzman"
				},
				{
					code: "AL11-A ",
					owner: "JOSE ENRIQUE NUÑEZ CAMPOS ",
					size: "12.60 X 5.00 ",
					type: "Unipolar 2 Caras ",
					price: "1,000.00",
					pricelow: "1,000.00",
					way: "SAN JOSE - CALDERA ",
					title: "AUTOPISTA GENERAL CAÑAS",
					orientation: "Horizontal ",
					client: "NO HAY ROTULO INSTALADO",
					state: "Inactiva ",
					registred: "7/22/14",
					user: "oguzman"
				},
				{
					code: "AL11-C ",
					owner: "JOSE ENRIQUE NUÑEZ CAMPOS ",
					size: "12.60 X 5.00 ",
					type: "Unipolar 2 Caras",
					price: "950.00",
					pricelow: "950.00",
					way: "CALDERA - SAN JOSE ",
					title: "AUTOPISTA GENERAL CAÑAS",
					orientation: "Horizontal ",
					client: "NO HAY ROTULO INSTALADO",
					state: "Inactiva ",
					registred: "5/24/18",
					user: "oguzman"
				},
				{
					code: "AL12-A ",
					owner: "JUAN BAUTISTA ARAYA CAMPOS",
					size: "12.60 X 5.00 ",
					type: "Unipolar 2 Caras",
					price: "950.00",
					pricelow: "950.00",
					way: "SAN JOSE - CALDERA ",
					title: "AUTOPISTA GENERAL CAÑAS",
					orientation: "Horizontal ",
					start: "12/1/16",
					due: "6/15/18",
					client: "LOS SUEÑOS MARRIOTT",
					state: "Arrendada",
					registred: "1/18/18",
					user: "oguzman"
				},
				{
					code: "AL12-C ",
					owner: "JUAN BAUTISTA ARAYA CAMPOS",
					size: "12.60 X 5.00 ",
					type: "Unipolar 2 Caras",
					price: "950.00",
					pricelow: "950.00",
					way: "CALDERA - SAN JOSE ",
					title: "AUTOPISTA GENERAL CAÑAS",
					orientation: "Horizontal ",
					start: "2/14/18",
					due: "2/14/19",
					client: "LOS SUEÑOS MARRIOTT",
					state: "Arrendada",
					registred: "3/5/18",
					user: "oguzman"
				}
			]
		},
		actions: {
			// Use getActions to call a function within a fuction
			exampleFunction: () => {
				getActions().changeColor(0, "orange");
			},

			getMessage: () => {
				// fetching data from the backend
				fetch(process.env.BACKEND_URL + "/api/hello")
					.then(resp => resp.json())
					.then(data => setStore({ message: data.message }))
					.catch(error => console.log("Error loading message from backend", error));
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			}
		}
	};
};

export default getState;
