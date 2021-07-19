import { useEffect, useState } from "react";
import { useRouteMatch } from "react-router-dom";
import { api } from "../../utils/api";

const Licenses = () => {
  let { path, url } = useRouteMatch();

  const [data, setData] = useState({
    licenses: [],
    loading: true,
    error: false,
  });

  useEffect(() => {
    let callification = async () => {
      await api
        .getLicenses()
        .then((response) => {
          setData({ licenses: response, loading: false });
        })
        .catch((error) =>
          setData({ licenses: [], loading: false, error: error })
        );
    };
    callification();
  }, []);

  if (data.loading) {
    return <>Loading...</>;
  } else {
    return (
      <div>
        <h2>Licenses</h2>
        <ul>
          {data.licenses.map((item) => (
            <li key={item.id}>
              {item.id} {item.software}
            </li>
          ))}
        </ul>
      </div>
    );
  }
};

export default Licenses;
