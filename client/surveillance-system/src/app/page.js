"use client";
import React from "react";
import { Container, Row, Col, Button } from "react-bootstrap";
import ReactPlayer from "react-player";

const Home = () => {
  const cameras = [
    {
      id: 1,
      name: "Room 1",
      url: "https://www.youtube.com/watch?v=QDX-1M5Nj7s",
    },
    {
      id: 2,
      name: "Room 2",
      url: "https://www.youtube.com/watch?v=QDX-1M5Nj7s",
    },
    {
      id: 3,
      name: "Room 3",
      url: "https://www.youtube.com/watch?v=QDX-1M5Nj7s",
    },
    {
      id: 4,
      name: "Room 4",
      url: "https://www.youtube.com/watch?v=QDX-1M5Nj7s",
    },
  ];

  const [currentCameras, setCurrentCameras] = React.useState([
    cameras[0],
    cameras[1],
    cameras[2],
    cameras[3],
  ]);

  const handleCameraChange = (camera) => {
    const index = currentCameras.findIndex((c) => c.id === camera.id);
    if (index === -1) return;

    const updatedCameras = [...currentCameras];
    updatedCameras[index] = camera;
    setCurrentCameras(updatedCameras);
  };

  return (
    <div
      style={{
        backgroundColor: "#F5810F",
        minHeight: "100vh",
        padding: "20px",
      }}
    >
      <Container>
        <h1
          className="text-center"
          style={{ fontSize: "20px", color: "white" }}
        >
          Surveillance Camera Dashboard
        </h1>
        <Row>
          <Col xs={12} md={3}>
            {/* Left Dashboard */}
            <div
              style={{
                backgroundColor: "white",
                padding: "20px",
                display: "flex",
                flexDirection: "row",
                flexWrap: "wrap",
                justifyContent: "center",
              }}
            >
              {cameras.map((camera) => (
                <Button
                  key={camera.id}
                  variant={
                    currentCameras.some((c) => c.id === camera.id)
                      ? "primary"
                      : "light"
                  }
                  onClick={() => handleCameraChange(camera)}
                  style={{ marginBottom: "10px", marginRight: "10px" }}
                >
                  {camera.name}
                </Button>
              ))}
            </div>
          </Col>
          <Col xs={12} md={9}>
            {/* Video View */}
            <div
              style={{
                backgroundColor: "white",
                padding: "20px",
                display: "grid",
                gridTemplateColumns: "repeat(2, 1fr)",
                gridTemplateRows: "repeat(2, 1fr)",
                gap: "20px",
              }}
            >
              {currentCameras.map((camera) => (
                <div key={camera.id}>
                  <ReactPlayer
                    url={camera.url}
                    width="100%"
                    maxHeight="700px"
                    controls
                  />
                </div>
              ))}
            </div>
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default Home;
