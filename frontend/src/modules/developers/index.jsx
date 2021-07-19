import { useEffect, useState } from "react";
import { useRouteMatch } from "react-router-dom";
import { api } from "../../utils/api";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  useParams,
} from "react-router-dom";

const Developers = () => {
  let { path, url } = useRouteMatch();

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
          console.log(response);
          setData({ developers: response, loading: false });
        })
        .catch((error) =>
          setData({ developers: [], loading: false, error: error })
        );
    };
    callification();
  }, []);

  if (data.loading) {
    return <>Loading...</>;
  } else {
    return (
      <>
        <h2>Developers</h2>
        <Switch>
          <Route exact path={path}>
            <DevelopersList developers={data.developers} />
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
  console.log(developers, devId, item);
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

export default Developers;
