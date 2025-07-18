import {
  DataTable,
  DateField,
  List,
  Show,
  SimpleShowLayout,
  TextField,
  UrlField,
  Edit,
  SimpleForm,
  TextInput,
  Create,
  required,
} from "react-admin";

export const DriverList = () => (
  <List>
    <DataTable>
      <DataTable.Col source="id" />
      <DataTable.Col source="driver_ref" />
      <DataTable.Col source="number" />
      <DataTable.Col source="code" />
      <DataTable.Col source="forename" />
      <DataTable.Col source="surname" />
      <DataTable.Col source="dob">
        <DateField source="dob" />
      </DataTable.Col>
      <DataTable.Col source="nationality" />
      <DataTable.Col source="url">
        <UrlField source="url" />
      </DataTable.Col>
    </DataTable>
  </List>
);

export const DriverShow = () => (
  <Show>
    <SimpleShowLayout>
      <TextField source="id" />
      <TextField source="driver_ref" />
      <DateField source="number" />
      <TextField source="code" />
      <TextField source="forename" />
      <TextField source="surname" />
      <DateField source="dob" />
      <TextField source="nationality" />
      <UrlField source="url" />
    </SimpleShowLayout>
  </Show>
);

export const DriverEdit = () => (
  <Edit>
    <SimpleForm>
      <TextInput disabled source="id" />
      <TextInput source="driver_ref" validate={required()} />
      <TextInput source="number" validate={required()} />
      <TextInput source="code" validate={required()} />
      <TextInput source="forename" validate={required()} />
      <TextInput source="surname" validate={required()} />
      <TextInput source="dob" label="Date of Birth (YYYY-MM-DD)" validate={required()} />
      <TextInput source="nationality" validate={required()} />
      <TextInput source="url" fullWidth validate={required()} />
    </SimpleForm>
  </Edit>
);

export const DriverCreate = () => (
  <Create>
    <SimpleForm>
      <TextInput source="driver_ref" validate={required()} />
      <TextInput source="number" validate={required()} />
      <TextInput source="code" validate={required()} />
      <TextInput source="forename" validate={required()} />
      <TextInput source="surname" validate={required()} />
      <TextInput source="dob" label="Date of Birth (YYYY-MM-DD)" validate={required()} />
      <TextInput source="nationality" validate={required()} />
      <TextInput source="url" fullWidth validate={required()} />
    </SimpleForm>
  </Create>
);
