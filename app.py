import os
import click
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from pydantic import BaseModel, ValidationError
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

class UserData(BaseModel):
    id: int
    name: str
    username: str
    email: str

def fetch_and_validate_data():
    print("Fetching external data...")
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=5)
        response.raise_for_status()
        user = UserData(**response.json())
        print(f"Validated user data for: {user.name}")
        return user
    except (requests.exceptions.RequestException, ValidationError) as e:
        print(f"Error: {e}")
        return None

def simulate_encryption(data_string: str):
    print("Simulating data encryption...")
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    print(f"Encrypted payload: {cipher_suite.encrypt(data_string.encode())[:30]}...")

def generate_and_visualize(samples: int):
    print(f"Generating analytics for {samples} samples...")
    dates = pd.date_range("2026-01-01", periods=samples)
    df = pd.DataFrame(np.random.randn(samples, 2), index=dates, columns=['Alpha', 'Beta'])
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Alpha'], label='Alpha', marker='o')
    plt.plot(df.index, df['Beta'], label='Beta', marker='x')
    plt.legend()
    os.makedirs('output', exist_ok=True)
    plt.savefig('output/chart.png')
    print("Artifact saved to output/chart.png")

@click.command()
@click.option('--samples', default=10, help='Number of data points.')
@click.option('--fetch/--no-fetch', default=True, help='Fetch API data.')
def cli(samples, fetch):
    print(f"API Key configured: {'Yes' if os.getenv('SECRET_API_KEY') else 'No'}")
    if fetch and (user := fetch_and_validate_data()):
        simulate_encryption(user.email)
    generate_and_visualize(samples)
    print("Execution complete.")

if __name__ == "__main__":
    cli()