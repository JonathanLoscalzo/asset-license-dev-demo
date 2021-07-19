import { useEffect, useState } from "react";
import {
  useRouteMatch,
} from "react-router-dom";
import { api } from "../../utils/api";

const Assets = () => {
  let { path, url } = useRouteMatch();

  const [data, setData] = useState({
    assets: [],
    loading: true,
    error: false,
  });

  useEffect(() => {
    let callification = async () => {
      await api
        .getAssets()
        .then((response) => {
          setData({ assets: response, loading: false });
        })
        .catch((error) =>
          setData({ assets: [], loading: false, error: error })
        );
    };
    callification();
  }, []);

  if (data.loading) {
    return <>Loading...</>;
  } else {
    return (
      <div>
        <h2>Assets</h2>
        <ul>
          {data.assets.map((item) => (
            <li key={item.id}>{item.id} </li>
          ))}
        </ul>
      </div>
    );
  }
};

export default Assets;