import { useEffect, useState } from "react";
import { useRouteMatch, useHistory } from "react-router-dom";
import { api } from "../../utils/api";
import { Switch, Route, Link, useParams } from "react-router-dom";
import {
  Button,
  Form,
  FormGroup,
  Label,
  Input,
  Row,
  FormFeedback,
} from "reactstrap";
import { useFormik } from "formik";

import * as Yup from "yup";

const Developers = () => {
  let { path } = useRouteMatch();

  const [data, setData] = useState({
    developers: [],
    loading: true,
    error: false,
  });

  useEffect(() => {
    let callification = async () => {
      await api
        .getDevelopers()
        .then((response) => {
          setData({ developers: response, loading: false });
        })
        .catch((error) =>
          setData({ developers: [], loading: false, error: error })
        );
    };
    callification();
  }, [data.loading]);

  if (data.loading) {
    return <>Loading...</>;
  } else {
    return (
      <>
        <h2>Developers</h2>
        <ul>
          <li>
            <Link to={`${path}/create`}>Create</Link>
          </li>
        </ul>
        <Switch>
          <Route exact path={path}>
            <DevelopersList developers={data.developers} />
          </Route>

          <Route exact path={`${path}/create`}>
            <DeveloperCreate
              setData={({ loading }) => setData({ ...data, loading: loading })}
            />
          </Route>

          <Route path={`${path}/:devId`}>
            <DeveloperSingle developers={data.developers} />
          </Route>
        </Switch>
      </>
    );
  }
};

const DevelopersList = ({ developers }) => {
  let { url } = useRouteMatch();

  return (
    <ul>
      {developers.map((item) => (
        <li key={item.id}>
          <Link to={`${url}/${item.id}`}> MongoID:{item.id}</Link> - Name:
          {item.fullname} - Active: {item.active ? "Yes" : "No"} - Licenses:
          {item.licenses.join(", ")} - Assets: {item.assets.join(", ")}
        </li>
      ))}
    </ul>
  );
};

const DeveloperSingle = ({ developers }) => {
  let { devId } = useParams();
  let item = developers.filter((d) => d.id === devId)[0];
  if (item === undefined) {
    return <></>;
  } else {
    return (
      <div>
        MongoID:{item.id} - Name:
        {item.fullname} - Active: {item.active ? "Yes" : "No"} - Licenses:
        {item.licenses && item.licenses.join(", ")}- Assets:{" "}
        {item.assets && item.assets.join(", ")}
      </div>
    );
  }
};

const DeveloperCreate = ({ setData, ...props }) => {
  const history = useHistory();

  const validationSchema = Yup.object().shape({
    fullname: Yup.string()
      .min(2, "Too Short!")
      .max(50, "Too Long!")
      .required("Required"),
    active: Yup.bool().required("Required"),
  });

  const formik = useFormik({
    initialValues: {
      fullname: "",
      active: true,
    },
    validationSchema,
    onSubmit: (values) => {
      api
        .createDeveloper({ fullname: values.fullname, active: values.active })
        .then(() => {
          setData({ loading: true });
          history.push("/developers");
        });
    },
  });

  return (
    <Row>
      <Form onSubmit={formik.handleSubmit}>
        <FormGroup>
          <Label for="exampleEmail">Fullname</Label>
          <Input
            type="text"
            name="fullname"
            id="fullname"
            placeholder="fullname"
            onChange={formik.handleChange}
            value={formik.values.fullname}
            invalid={formik.errors.fullname}
          />
          {formik.errors.fullname && (
            <FormFeedback>{formik.errors.fullname}</FormFeedback>
          )}
        </FormGroup>
        <FormGroup check>
          <Label check>
            <Input
              type="checkbox"
              name="active"
              onChange={formik.handleChange}
              value={formik.values.active}
            />{" "}
            Active?
          </Label>
        </FormGroup>
        <Button type="submit">Submit</Button>
      </Form>
    </Row>
  );
};

export default Developers;
