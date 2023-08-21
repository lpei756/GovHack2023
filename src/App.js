import React, { useEffect, useRef, useState } from "react";
import mapboxgl from "!mapbox-gl";
import "mapbox-gl/dist/mapbox-gl.css";
import "./index.css";
import { Layout } from "./Layout";

function App() {
  mapboxgl.accessToken =
    "pk.eyJ1IjoibHBlaTc1NiIsImEiOiJjbGxoOHozODAwOHpxM2xsd2ZsM2xzOWl3In0.Gh9K818BkemD9i3PrQblrQ";
  const mapContainer = useRef(null);
  const map = useRef(null);
  const [lng, setLng] = useState(172.6362);
  const [lat, setLat] = useState(-43.5321);
  const [zoom, setZoom] = useState(11);

  useEffect(() => {
    if (map.current) return; // initialize map only once
    map.current = new mapboxgl.Map({
      container: mapContainer.current,
      style: "mapbox://styles/mapbox/satellite-streets-v12",
      center: [lng, lat],
      zoom: zoom,
    });

    map.current.on("load", function () {
      map.current.loadImage("/Build.png", function (error, image) {
        if (error) throw error;
        map.current.addImage("build-icon", image);

        map.current.loadImage('/Repair.png', function (error, image) {
          if (error) throw error;
          map.current.addImage('repair-icon', image);
      });
      map.current.loadImage('/Water.png', function (error, image) {
          if (error) throw error;
          map.current.addImage('water-icon', image);
      });
      map.current.loadImage('/Power.png', function (error, image) {
          if (error) throw error;
          map.current.addImage('power-icon', image);
      });

        // Continue with adding sources and layers after image is loaded
        Promise.all([
          fetch("DP_Scheduled_Activity_(OpenData).geojson").then((response) =>
            response.json()
          ),
          fetch("DP_Outline_Development_(OpenData).geojson").then((response) =>
            response.json()
          ),
          fetch("WaterShutoffs.geojson").then((response) => response.json()),
          fetch("PowerOutages.geojson").then((response) => response.json()),
        ]).then(
          ([
            scheduledActivityData,
            outlineDevelopmentData,
            waterShutoffsData,
            powerOutagesData,
          ]) => {
            map.current.addSource("scheduled-activities", {
              type: "geojson",
              data: scheduledActivityData,
            });

            map.current.addSource("outline-developments", {
              type: "geojson",
              data: outlineDevelopmentData,
            });
            map.current.addSource("water-shutoffs", {
              type: "geojson",
              data: waterShutoffsData,
            });
            map.current.addSource("power-outages", {
              type: "geojson",
              data: powerOutagesData,
            });

            map.current.addLayer({
              id: "activities-icons",
              type: "symbol",
              source: "scheduled-activities",
              layout: {
                "icon-image": [
                  "match",
                  ["get", "LegalStatus"],
                  "Operative",
                  "repair-icon",
                  "", // default
                ],
                "icon-size": 0.1,
              },
            });

            map.current.addLayer({
              id: "outline-development-icons",
              type: "symbol",
              source: "outline-developments",
              layout: {
                "icon-image": [
                  "match",
                  ["get", "LegalStatus"],
                  "Operative",
                  "build-icon",
                  "", // default
                ],
                "icon-size": 0.12,
              },
            });

            map.current.addLayer({
              id: "water-icons",
              type: "symbol",
              source: "water-shutoffs",
              layout: {
                "icon-image": [
                  "match",
                  ["get", "feature"],
                  "watershutoffs",
                  "water-icon",
                  "", // default
                ],
                "icon-size": 0.1,
              },
            });

            map.current.addLayer({
              id: "power-icons",
              type: "symbol",
              source: "power-outages",
              layout: {
                "icon-image": [
                  "match",
                  ["get", "feature"],
                  "poweroutage",
                  "power-icon",
                  "", // default
                ],
                "icon-size": 0.1,
              },
            });

            map.current.on("click", "activities-icons", (e) => {
              var feature = e.features[0];
              var popup = new mapboxgl.Popup()
                .setLngLat(e.lngLat)
                .setHTML(
                  `<strong>${feature.properties.ActivityName}</strong><br>` +
                    `Type: ${feature.properties.Type}<br>` +
                    `Activity Number: ${feature.properties.ActivityNumber}<br>` +
                    `Legal Status: ${feature.properties.LegalStatus}`
                )
                .addTo(map.current);
            });

            map.current.on("click", "outline-development-icons", (e) => {
              var feature = e.features[0];
              var popup = new mapboxgl.Popup()
                .setLngLat(e.lngLat)
                .setHTML(
                  `<strong>${feature.properties.Name}</strong><br>` +
                    `Type: ${feature.properties.Type}<br>` +
                    `Activity Number: ${feature.properties.DPOutlineDevelopmentID}<br>` +
                    `Legal Status: ${feature.properties.LegalStatus}`
                )
                .addTo(map.current);
            });

            map.current.on("click", "water-icons", (e) => {
              var feature = e.features[0];
              var popup = new mapboxgl.Popup()
                .setLngLat(e.lngLat)
                .setHTML(
                  `<strong>${feature.properties.Address}</strong><br>` +
                    `Is active: ${feature.properties.IsActive}<br>` +
                    `Shut down type: ${feature.properties.ShutdownType}<br>` +
                    `Est hours off${feature.properties.LegalStatus}`
                )
                .addTo(map.current);
            });

            // Display a popup on click for Power Outages
            map.current.on("click", "power-icons", (e) => {
              const feature = e.features[0];
              const popup = new mapboxgl.Popup()
                .setLngLat(e.lngLat)
                .setHTML(
                  `<strong>${feature.properties.feature}</strong><br>` +
                    `Comment: ${feature.properties.comment}<br>` +
                    `Cause: ${feature.properties.cause}<br>` +
                    `Area: ${feature.properties.area}`
                )
                .addTo(map.current);
            });

            return () => {
              map.current.remove();
            };
          }
        );
      });
    });
  }, []);

  return (
    <Layout>
      <div ref={mapContainer} className="map-container" />
      <div className="legend">
        <h4>LEGEND</h4>
        <div>
          <img src="/Build.png" alt="Repair" width="20px" />
          <span>Under Building</span>
        </div>
        <div>
          <img src="/Repair.png" alt="Repair" width="20px" />
          <span>Under Repairing</span>
        </div>
        <div>
          <img src="/Water.png" alt="Water" width="20px" />
          <span>Water Shutoffs</span>
        </div>
        <div>
          <img src="/Power.png" alt="Power" width="20px" />
          <span>Power Outages</span>
        </div>
      </div>
    </Layout>
  );
}

export default App;
