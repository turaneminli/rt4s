"use client";
import React, { useState } from "react";
import { Container, Row, Col, Button } from "react-bootstrap";
import ReactPlayer from "react-player";
import Image from "next/image";

const Home = () => {
  const cameras = [
    {
      id: 1,
      name: "Room 1",
      url: "https://www.youtube.com/watch?v=QDX-1M5Nj7s",
      path: "/Picture2.png",
    },
    {
      id: 2,
      name: "Room 2",
      url: "https://www.youtube.com/watch?v=QDX-1M5Nj7s",
      path: "/Picture1.png",
    },
  ];

  const [currentCameras, setCurrentCameras] = useState(cameras.slice(0, 2));
  const [showNotification, setShowNotification] = useState(false);

  const handleCameraChange = (camera) => {
    const index = currentCameras.findIndex((c) => c.id === camera.id);
    if (index === -1) return;

    const updatedCameras = [...currentCameras];
    updatedCameras[index] = camera;
    setCurrentCameras(updatedCameras);
  };

  const handleNotificationClick = () => {
    setShowNotification(true);
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
                color: "black",
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
              <Button
                style={{
                  backgroundColor: "#F84F31",
                  color: "white",
                  borderRadius: "10px",
                  marginLeft: "10px",
                  width: "190px",
                }}
                onClick={handleNotificationClick}
              >
                Show Notifications
              </Button>
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
                  <Image src={camera.path} width={500} height={500} />
                </div>
              ))}
            </div>
          </Col>
        </Row>

        {showNotification && (
          <div
            style={{
              position: "fixed",
              top: "20px",
              right: "20px",
              backgroundColor: "red",
              color: "white",
              padding: "10px",
              borderRadius: "5px",
            }}
          >
            New notification! Warning!
          </div>
        )}
      </Container>
    </div>
  );
};

export default Home;
