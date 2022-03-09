import React, { useContext, useState } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";
import "../../styles/app.scss";

import { Col, Row, Form, Table } from "react-bootstrap";
import Modalbox from "../component/modal";

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
				<Table>
					<th className="listheader list-group-item d-flex">
						<div className="col-1">Código</div>
						<div className="col-1">Estatus</div>
						<div className="col-2">Cliente</div>
						<div className="col-4">Ubicación</div>
						<div className="col-4">Propietario</div>
					</th>
					{data.map((item, index) => {
						return (
							<tr
								key={index}
								className={
									item.status === "Arrendada"
										? "arrendada list-group-item"
										: "disponible list-group-item"
								}>
								<td className="col-1 codeButton">
									<Link to={"/sitedetail/" + index}>
										<span>{item.code}</span>
									</Link>
								</td>

								<td className="col-1">{item.status}</td>
								<td className="col-2">{item.client}</td>
								<td className="col-4">{item.owner}</td>
								<td className="col-4">{item.address}</td>
							</tr>
						);
					})}
				</Table>
			</div>
			<br />
			<Link to="/">
				<button className="btn btn-primary">Regresar</button>
			</Link>
			<Modalbox />
		</div>
	);
};
