import React, { useContext } from "react";
import { useParams } from "react-router-dom";
import { Context } from "../store/appContext";

import { Form } from "react-bootstrap";

export const Siteowner = () => {
	const { store, actions } = useContext(Context);
	const params = useParams();

	return (
		<div>
			<Form.Group>
				<label htmlFor="inputAddress">Propietario</label>
				<input type="text" className="form-control" id="inputAddress" placeholder=""></input>
			</Form.Group>
			<Form.Group>
				<label htmlFor="inputAddress">Dirección</label>
				<input type="text" className="form-control" id="inputAddress" placeholder=""></input>
			</Form.Group>
			<Form.Group>
				<label htmlFor="inputAddress">Teléfono</label>
				<input type="text" className="form-control" id="inputAddress" placeholder=""></input>
			</Form.Group>
			<Form.Group>
				<label htmlFor="inputAddress">Email</label>
				<input type="text" className="form-control" id="inputAddress" placeholder=""></input>
			</Form.Group>
		</div>
	);
};
