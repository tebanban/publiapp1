import React, { useContext, useState } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";
import "../../styles/app.scss";

import { Col, Row, Form } from "react-bootstrap";

export const App = () => {
	const { store, actions } = useContext(Context);
	const [query, setQuery] = useState("");

	const data = store.site.filter(index => {
		if (query === "") {
			return index;
		} else if (index.code.toLowerCase().includes(query.toLowerCase())) {
			return index;
		} else if (index.status.toLowerCase().includes(query.toLowerCase())) {
			return index;
		}
	});

	return (
		<div>
			<div className="container">
				<Row className="mb-1">
					<Col md={4}>
						<input
							onChange={e => setQuery(e.target.value)}
							type="text"
							className="form-control"
							id="inputSearch"
							placeholder="Search"></input>
					</Col>
					<Col md={4}>
						<Form.Group>
							<select onChange={e => setQuery(e.target.value)} id="inputState" className="form-control">
								<option defaultValue>Filtrar por estado...</option>
								<option>Arrendada</option>
								<option>Inactiva</option>
								<option>Reservada</option>
								<option>Deshabilitada</option>
							</select>
						</Form.Group>
					</Col>
					<Col md={4}>
						<Form.Group>
							<select id="inputState" className="form-control">
								<option defaultValue>Filtrar por provincia...</option>
								<option>San José</option>
								<option>Alajuela</option>
								<option>Heredia</option>
								<option>Cartago</option>
								<option>Puntarenas</option>
								<option>Guanacaste</option>
								<option>Limón</option>
							</select>
						</Form.Group>
					</Col>
				</Row>
				<Row className="listheader list-group-item d-flex justify-content-between">
					<div className="col-1"> Código </div>
					<div className="col-3"> Propietario</div>
					<div className="col-3"> Ubicación</div>
					<div className="col-3"> Estado</div>
					<div className="col-2"> Cliente</div>
				</Row>
				{data.map((item, index) => {
					return (
						<Row
							key={index}
							className={
								item.status === "Arrendada" ? "arrendada list-group-item" : "disponible list-group-item"
							}>
							<div className="col-1">
								<Link to={"/sitedetail/" + index}>
									<span>{item.code}</span>
								</Link>
							</div>

							<div className="col-3">{item.owner}</div>
							<div className="col-3">{item.address}</div>
							<div className="col-3">{item.status}</div>
							<div className="col-2">{item.client}</div>
						</Row>
					);
				})}
			</div>
			<br />
			<Link to="/">
				<button className="btn btn-primary">Regresar</button>
			</Link>
		</div>
	);
};
