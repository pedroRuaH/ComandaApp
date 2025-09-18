// /static/js/main.js
import * as THREE from "https://cdn.skypack.dev/three@0.129.0/build/three.module.js";
import { OrbitControls } from "https://cdn.skypack.dev/three@0.129.0/examples/jsm/controls/OrbitControls.js";
import { STLLoader } from "https://cdn.skypack.dev/three@0.129.0/examples/jsm/loaders/STLLoader.js";

console.log("main.js module loaded");

// Create scene, camera and renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);
const renderer = new THREE.WebGLRenderer({ alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);

// Set up OrbitControls
const controls = new OrbitControls(camera, renderer.domElement);
camera.position.z = 5;

// Add a directional light
const topLight = new THREE.DirectionalLight(0xffffff, 1);
scene.add(topLight);

/**
 * loadSTL(url)
 * Loads an STL file from the given URL, centers its geometry, and adds the mesh to the scene.
 */
function loadSTL(url) {
  console.log(`loadSTL() called with URL: ${url}`);
  const loader = new STLLoader();
  loader.load(
    url,
    (geometry) => {
      console.log("STL file loaded successfully");
      geometry.computeBoundingBox();
      const bbox = geometry.boundingBox;
      console.log("Original BoundingBox:", bbox);
      const center = new THREE.Vector3();
      bbox.getCenter(center);
      geometry.translate(-center.x, -center.y, -center.z);
      console.log("Geometry centered");
      const material = new THREE.MeshNormalMaterial();
      const mesh = new THREE.Mesh(geometry, material);
      scene.add(mesh);
      console.log("Mesh added to scene");
      animate();
    },
    (xhr) => {
      // Log loading progress (if available)
      if (xhr.total) {
        console.log(`STL loading progress: ${(xhr.loaded / xhr.total) * 100}%`);
      } else {
        console.log("STL loading progress event", xhr);
      }
    },
    (error) => {
      console.error("Error loading STL file:", error);
    }
  );
}

/**
 * animate()
 * Runs the render loop.
 */
function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}

export { loadSTL, scene, renderer, camera };
