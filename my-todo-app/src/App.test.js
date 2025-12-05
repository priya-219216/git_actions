import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders todo heading", () => {
  render(<App />);
  const heading = screen.getByText(/simple todo app/i);
  expect(heading).toBeInTheDocument();
});
