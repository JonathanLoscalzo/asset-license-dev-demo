import { useEffect, useState } from "react";
import { useRouteMatch } from "react-router-dom";
import { api } from "../../utils/api";

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
      <div>
        <h2>Developers</h2>
        <ul>
          {data.developers.map((item) => (
            <li key={item.id}>
              MongoID:{item.id} - Name:{item.fullname} - Active:{" "}
              {item.active ? "Yes" : "No"} - Licenses:{item.licenses.join(", ")}{" "}
              - Assets: {item.assets.join(", ")}
            </li>
          ))}
        </ul>
      </div>
    );
  }
};

export default Developers;
