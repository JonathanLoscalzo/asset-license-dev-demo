import React from "react";
import { useFormik } from "formik";
import { Button, Form, FormGroup, Label, Input } from "reactstrap";
import { api } from "../../utils/api.ts";

export function AuthPage() {
  const formik = useFormik({
    initialValues: {
      username: "admin",
      password: "secure",
    },
    onSubmit: async (values) => {
      await api.login(values.username, values.password);
    },
  });

  return (
    <Form onSubmit={formik.handleSubmit}>
      <FormGroup>
        <Label for="exampleEmail">Username</Label>
        <Input
          type="texxt"
          name="username"
          id="usernameid"
          placeholder="Username hint: admin"
          onChange={formik.handleChange}
          value={formik.values.username}
        />
      </FormGroup>
      <FormGroup>
        <Label for="examplePassword">Password</Label>
        <Input
          type="password"
          name="password"
          id="examplePassword"
          placeholder="password hint: secure"
          onChange={formik.handleChange}
          value={formik.values.password}
        />
      </FormGroup>
      <Button>Submit</Button>
    </Form>
  );
}
