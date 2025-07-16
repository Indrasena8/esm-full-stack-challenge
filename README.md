# ESM FullStack Challenge
## ✅ Task 1 – Implement Driver CRUD Functionality

As part of the ESM FullStack challenge, I implemented Create, Update, and Delete operations for the **Drivers** resource. This involved modifying both the FastAPI backend and the React-Admin frontend.

### 🔧 Backend (FastAPI - `routers/drivers.py`)

- Created a `DriverIn` Pydantic model to handle driver input data.
- Added the following endpoints:
  - `POST /drivers` – Inserts a new driver into the database.
  - `PUT /drivers/{id}` – Updates an existing driver's information based on ID.
  - `DELETE /drivers/{id}` – Deletes a driver entry if it exists.
- Used a helper function `row_to_dict()` to safely map database rows to dictionaries for response parsing.
- Reused existing GET routes for listing and retrieving individual drivers.

### 💻 Frontend (React Admin - `pages/drivers.tsx`)

- Implemented `DriverCreate` and `DriverEdit` views using `SimpleForm` and `TextInput`.
- Required fields are validated using `validate={required()}` for inputs like `driver_ref`, `forename`, `surname`, and `dob`.
- Existing components `DriverList` and `DriverShow` were retained and integrated with the new create/edit functionality.

These changes made the "Drivers" section of the app fully editable and CRUD-enabled through the admin dashboard, using the existing database schema without needing structural updates.
