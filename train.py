import torch
import torch.nn as nn
from torch.utils.tensorboard import SummaryWriter
from utils.logger import setup_logger
from utils.seed import set_seed
from utils.args import parse_args
import numpy as np
import os

# Simple neural network for demonstration
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(10, 50)
        self.fc2 = nn.Linear(50, 1)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

def train():
    args = parse_args()
    
    # Set random seed
    set_seed(args.seed)
    
    # Setup logger
    logger = setup_logger(args.log_dir, args.experiment_name)
    
    # Setup TensorBoard writer
    writer = SummaryWriter(log_dir=os.path.join(args.log_dir, args.experiment_name))
    
    # Create model directory
    os.makedirs(args.model_dir, exist_ok=True)
    
    # Initialize model, loss, and optimizer
    model = SimpleNet()
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=args.learning_rate)
    
    logger.info(f"Starting training for {args.experiment_name}")
    logger.info(f"Parameters: epochs={args.epochs}, batch_size={args.batch_size}, "
                f"learning_rate={args.learning_rate}, seed={args.seed}")
    
    # Training loop
    for epoch in range(args.epochs):
        # Generate dummy data for demonstration
        inputs = torch.randn(args.batch_size, 10)
        targets = torch.randn(args.batch_size, 1)
        
        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        
        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        # Log metrics
        logger.info(f"Epoch [{epoch+1}/{args.epochs}], Loss: {loss.item():.4f}")
        writer.add_scalar('Loss/train', loss.item(), epoch)
        
        # Save model checkpoint
        if (epoch + 1) % 5 == 0:
            checkpoint_path = os.path.join(args.model_dir, f'checkpoint_epoch_{epoch+1}.pth')
            torch.save(model.state_dict(), checkpoint_path)
            logger.info(f"Saved checkpoint: {checkpoint_path}")
    
    # Log example metrics to TensorBoard
    writer.add_scalar('Final/Loss', loss.item(), epoch)
    
    # Close TensorBoard writer
    writer.close()
    logger.info("Training completed")

if __name__ == "__main__":
    train()