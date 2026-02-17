"""
Configuration file for Kira Health Assistant training.
Modify these parameters to experiment with different settings.
"""

class TrainingConfig:
    """Configuration for model training and fine-tuning."""
    
    # ==================== Model Selection ====================
    # Choose one of the following models
    MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"  # Recommended for Colab
    # MODEL_NAME = "google/gemma-2b"  # Alternative (requires access)
    # MODEL_NAME = "facebook/opt-1.3b"  # Another option
    
    # ==================== Dataset Configuration ====================
    DATASET_NAME = "medalpaca/medical_meadow_medical_flashcards"
    MAX_SAMPLES = 3000  # Number of samples to use (balance quality vs speed)
    TRAIN_SPLIT = 0.9   # 90% training, 10% validation
    
    # ==================== Tokenization ====================
    MAX_LENGTH = 512  # Maximum sequence length (context window)
    TRUNCATION = True
    PADDING = "max_length"
    
    # ==================== LoRA Configuration ====================
    # Low-Rank Adaptation parameters
    LORA_R = 16              # Rank of low-rank matrices (higher = more capacity)
    LORA_ALPHA = 32          # Scaling factor (typically 2x LORA_R)
    LORA_DROPOUT = 0.05      # Dropout for LoRA layers
    TARGET_MODULES = [       # Which modules to apply LoRA to
        "q_proj",
        "k_proj", 
        "v_proj",
        "o_proj"
    ]
    LORA_BIAS = "none"
    LORA_TASK_TYPE = "CAUSAL_LM"
    
    # ==================== Training Hyperparameters ====================
    # Experiment with these values
    LEARNING_RATE = 2e-4               # Learning rate (1e-4 to 5e-4 typical)
    BATCH_SIZE = 4                      # Per-device batch size
    GRADIENT_ACCUMULATION_STEPS = 4     # Effective batch = BATCH_SIZE * this
    NUM_EPOCHS = 3                      # Number of training epochs
    WARMUP_STEPS = 100                  # Learning rate warmup
    
    # ==================== Optimization ====================
    WEIGHT_DECAY = 0.01        # L2 regularization
    MAX_GRAD_NORM = 0.3        # Gradient clipping
    OPTIMIZER = "paged_adamw_8bit"  # Memory-efficient optimizer
    LR_SCHEDULER = "cosine"    # Learning rate schedule
    
    # ==================== Quantization ====================
    # 4-bit quantization for memory efficiency
    USE_4BIT = True
    BNB_4BIT_COMPUTE_DTYPE = "float16"
    BNB_4BIT_QUANT_TYPE = "nf4"
    BNB_4BIT_USE_DOUBLE_QUANT = True
    
    # ==================== Training Settings ====================
    LOGGING_STEPS = 10
    SAVE_STRATEGY = "epoch"
    EVALUATION_STRATEGY = "epoch"
    SAVE_TOTAL_LIMIT = 2
    FP16 = True  # Mixed precision training
    
    # ==================== Paths ====================
    OUTPUT_DIR = "./kira_health_assistant_output"
    CHECKPOINT_DIR = "./kira_checkpoints"
    FINAL_MODEL_DIR = "./kira_final_model"
    
    # ==================== Generation Parameters ====================
    # For inference
    MAX_NEW_TOKENS = 400
    TEMPERATURE = 0.7
    TOP_P = 0.9
    TOP_K = 50
    DO_SAMPLE = True
    REPETITION_PENALTY = 1.1
    
    # ==================== Prompt Template ====================
    SYSTEM_PROMPT = "You are Kira, a knowledgeable medical assistant. Provide accurate, helpful information about medical topics."
    
    PROMPT_TEMPLATE = """<|system|>
{system_prompt}</|system|>
<|user|>
{user_message}</|user|>
<|assistant|>
"""
    
    def __repr__(self):
        """String representation of config."""
        config_dict = {k: v for k, v in vars(self).items() 
                      if not k.startswith('_') and k.isupper()}
        return f"TrainingConfig({config_dict})"


# ==================== Experiment Presets ====================

class ExperimentConfigs:
    """Predefined experiment configurations."""
    
    @staticmethod
    def baseline():
        """Baseline configuration (Experiment 1)."""
        config = TrainingConfig()
        config.LEARNING_RATE = 2e-4
        config.LORA_R = 16
        config.LORA_ALPHA = 32
        return config
    
    @staticmethod
    def conservative():
        """Conservative training (Experiment 2)."""
        config = TrainingConfig()
        config.LEARNING_RATE = 1e-4  # Lower learning rate
        config.NUM_EPOCHS = 4         # More epochs
        return config
    
    @staticmethod
    def high_capacity():
        """Higher LoRA rank for more capacity (Experiment 3)."""
        config = TrainingConfig()
        config.LORA_R = 32            # Higher rank
        config.LORA_ALPHA = 64        # Adjusted alpha
        config.BATCH_SIZE = 2         # Smaller batch for memory
        config.GRADIENT_ACCUMULATION_STEPS = 8
        return config
    
    @staticmethod
    def fast_training():
        """Faster training for quick experiments."""
        config = TrainingConfig()
        config.MAX_SAMPLES = 1000     # Fewer samples
        config.NUM_EPOCHS = 2          # Fewer epochs
        config.BATCH_SIZE = 8          # Larger batch
        return config


# ==================== Usage Example ====================
if __name__ == "__main__":
    # Use baseline config
    config = ExperimentConfigs.baseline()
    print("=" * 60)
    print("TRAINING CONFIGURATION")
    print("=" * 60)
    print(f"Model: {config.MODEL_NAME}")
    print(f"Dataset: {config.DATASET_NAME}")
    print(f"Samples: {config.MAX_SAMPLES}")
    print(f"\nLoRA Configuration:")
    print(f"  Rank: {config.LORA_R}")
    print(f"  Alpha: {config.LORA_ALPHA}")
    print(f"  Dropout: {config.LORA_DROPOUT}")
    print(f"\nTraining Hyperparameters:")
    print(f"  Learning Rate: {config.LEARNING_RATE}")
    print(f"  Batch Size: {config.BATCH_SIZE}")
    print(f"  Gradient Accumulation: {config.GRADIENT_ACCUMULATION_STEPS}")
    print(f"  Effective Batch Size: {config.BATCH_SIZE * config.GRADIENT_ACCUMULATION_STEPS}")
    print(f"  Epochs: {config.NUM_EPOCHS}")
    print(f"\nOutput Directory: {config.OUTPUT_DIR}")
    print("=" * 60)
