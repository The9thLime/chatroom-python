# Chat Server and Client

## Overview

This project is a simple chat application implemented in Python. It consists of a server and a client program. The server handles multiple client connections and broadcasts messages between clients. Each client sees their own messages with a `[You]` prefix and other clients' messages with the sender's address.

## Features

- Multiple clients can connect to the server.
- Clients receive their own messages prefixed with `[You]`.
- Other clients receive messages with the sender's address.

## Prerequisites

- Python 3.x installed on your system.

## Getting Started

Follow these steps to run the server and client programs.

### Running the Server

1. **Navigate to the server directory**:

    ```bash
    cd ./server
    ```

2. **Start the server**:

    ```bash
    python3 server.py
    ```

    The server will start and listen for incoming connections on port `60601`.

### Running the Client

1. **Navigate to the client directory**:

    ```bash
    cd ./client
    ```

2. **Start the client**:

    ```bash
    python3 client.py
    ```

    The client will connect to the server running on `localhost` at port `60601`.

### Using the Chat Application

1. **Multiple clients**: You can start multiple instances of the client program to simulate multiple users.

2. **Sending Messages**: Type your messages in the terminal and press Enter. You will see your own messages with a `[You]` prefix, and other clients will see your messages with your address.

3. **Receiving Messages**: Messages from other clients will be displayed with the sender's address.

### Example

- **Client A** sends a message `"Hello everyone!"`.
- **Client A** sees: `[You] Hello everyone!`
- **Client B** sees: `[127.0.0.1:port] Hello everyone!`

## Troubleshooting

- **Connection Issues**: Ensure that the server is running before starting the client. Check for any firewall settings that might block the connection.

- **Message Duplication**: Ensure that the client-side code only displays messages it receives from the server and does not print the messages it sends.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
