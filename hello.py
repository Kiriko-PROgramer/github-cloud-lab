def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}! Welcome to GitHub cloud."

if __name__ == "__main__":
    print(greet("World"))
    print(greet("GitHub"))
EOF\
cat > hello.py << 'EOF'
def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}! Welcome to GitHub cloud."

if __name__ == "__main__":
    print(greet("World"))
    print(greet("GitHub"))
