
import pandas as pd
import numpy as np

class ChessPieceIdentifier:
    def __init__(self, probability_data):
        self.probability_data = probability_data

    def identify_piece(self, position, color):
        """
        Identify the chess piece based on its position and color using probabilities.
        
        Args:
            position (str): Position on the chessboard, e.g., 'e4'.
            color (str): Color of the piece, 'white' or 'black'.
        
        Returns:
            str: Name of the piece.
        """
        if position not in self.probability_data:
            return 'Unknown piece'
        
        piece_probabilities = self.probability_data[position].get(color, {})
        if not piece_probabilities:
            return 'Unknown piece'
        
        piece = max(piece_probabilities, key=piece_probabilities.get)
        return piece

def load_probability_data(filepath):
    """
    Load the probability data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file containing the probability data.
    
    Returns:
        dict: Nested dictionary with positions and piece probabilities.
    """
    df = pd.read_csv(filepath)
    probability_data = {}
    
    for _, row in df.iterrows():
        position = row['position']
        color = row['color']
        piece = row['piece']
        probability = row['probability']
        
        if position not in probability_data:
            probability_data[position] = {}
        if color not in probability_data[position]:
            probability_data[position][color] = {}
        
        probability_data[position][color][piece] = probability
    
    return probability_data

if __name__ == "__main__":
    filepath = 'data/processed/piece_probabilities.csv'
    probability_data = load_probability_data(filepath)
    identifier = ChessPieceIdentifier(probability_data)
    
    print(identifier.identify_piece('e4', 'white'))
    print(identifier.identify_piece('d4', 'black'))