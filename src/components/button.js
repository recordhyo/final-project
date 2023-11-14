function Button({
  label,
  className = "w-35 my-5 py-2 bg-my-color  text-white  hover:bg-my-color/70 rounded px-4",
  onClick,
  disabled,
}) {
  return (
    <button className={className} onClick={onClick} disabled={disabled}>
      {label}
    </button>
  );
}

export default Button;
