import argparse

def parse_args():
    """Parse command line arguments for training."""
    parser = argparse.ArgumentParser(description='Training script with experiment management')
    parser.add_argument('--experiment_name', type=str, default='default_experiment',
                        help='Name of the experiment')
    parser.add_argument('--seed', type=int, default=42,
                        help='Random seed for reproducibility')
    parser.add_argument('--epochs', type=int, default=10,
                        help='Number of training epochs')
    parser.add_argument('--batch_size', type=int, default=32,
                        help='Batch size for training')
    parser.add_argument('--learning_rate', type=float, default=0.001,
                        help='Learning rate for optimizer')
    parser.add_argument('--log_dir', type=str, default='logs',
                        help='Directory for saving logs')
    parser.add_argument('--model_dir', type=str, default='models',
                        help='Directory for saving model checkpoints')
    return parser.parse_args()