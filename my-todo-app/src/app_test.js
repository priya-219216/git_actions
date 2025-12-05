import { render, screen } from '@testing-library/react';
import App from './App';

test('renders heading', () => {
  render(<App />);
  const headingElement = screen.getByText(/todo app/i);
  expect(headingElement).toBeInTheDocument();
});
