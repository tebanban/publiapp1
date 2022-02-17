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
		}
	});
	console.log(query);
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
							<select id="inputState" className="form-control">
								<option defaultValue>Filtrar por estado...</option>
								<option>Alquilada</option>
								<option>Libre</option>
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
				<div className="listheader list-group-item d-flex justify-content-between">
					<div className="col-1"> Código </div>
					<div className="col-3"> Nombre</div>
					<div className="col-3"> Ubicación</div>
					<div className="col-3"> Contacto</div>
					<div className="col-1"> Accion</div>
				</div>
				{data.map((item, index) => {
					return (
						<div
							key={index}
							className="list-group-item d-flex justify-content-between"
							style={{ background: item.background }}>
							<div className="col-1">
								<Link to={"/sitedetail/" + index}>
									<span>{item.code}</span>
								</Link>
							</div>

							<div className="col-3">{item.title}</div>
							<div className="col-3">{item.address}</div>
							<div className="col-3">{item.contact}</div>

							<div className="col-1 btn btn-success" type="button">
								<Link to={"/sitedetail/" + index} className="link">
									<span>VER</span>
								</Link>
							</div>
						</div>
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
