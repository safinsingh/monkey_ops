# MonkeyOps

This repository contains a monorepo consisting of a frontend application built with React and a backend application using Flask. The frontend and backend are organized in separate directories within the repository.

## Frontend

The frontend application is located in the `/frontend` directory. It is built with React and utilizes [pnpm](https://pnpm.io/) as the package manager. To install the necessary dependencies, please follow these steps:

1. Ensure you have Node.js and pnpm installed on your machine.
2. Navigate to the `/frontend` directory in your terminal.
3. Run the following command to install the dependencies:

   ```bash
   pnpm install
   ```

Once the dependencies are installed, you can start the frontend application by running:

```bash
pnpm start
```

The frontend application is designed to automatically switch the backend URL based on whether it is running in production or locally. When running in production, it will connect to the deployed backend URL. However, when running locally, it will connect to `localhost`.

## Backend

The backend application is located in the `/backend` directory. It is built with Flask, a Python web framework. To install the necessary dependencies, please follow these steps:

1. Ensure you have Python and pip installed on your machine.
2. Navigate to the `/backend` directory in your terminal.
3. Run the following command to install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

Once the dependencies are installed, you can start the backend application by running:

```bash
python main.py
```

The backend application will be accessible at `http://localhost:8080`.

## Deployment

To deploy the application, follow the steps below:

1. Deploy the backend on AWS using a systemd service. The service file (`monkey-ops.service`) is located in the `/service` directory of this repository. Please refer to the AWS documentation to set up and configure the service properly.
2. Install Docker on the AWS instance to ensure compatibility with the backend.
3. Spawn AWS instances as needed, and the backend will work correctly.

For the frontend deployment, it is automated using GitHub Actions. The necessary configurations have already been provided. To deploy the frontend on GitHub Pages, follow these steps:

1. Push your changes to the repository's main branch.
2. GitHub Actions will automatically trigger the deployment process.
3. Once the deployment is complete, the frontend application will be accessible at the corresponding GitHub Pages URL.

If you need to change the API URL used by the frontend, you can do so by modifying the appropriate configuration file or environment variable in the codebase.

## Contributing

We welcome contributions to improve this project. Feel free to open issues or submit pull requests.

## License

This project is licensed under the [BSD 2-Clause License](LICENSE).
