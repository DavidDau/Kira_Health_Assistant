"""
Inference script for Kira Health Assistant.
Load a trained model and interact with it.
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import argparse
import warnings
warnings.filterwarnings('ignore')


class KiraHealthAssistant:
    """Wrapper class for Kira Health Assistant inference."""
    
    def __init__(self, model_path: str, base_model_name: str = None):
        """
        Initialize the Kira assistant.
        
        Args:
            model_path: Path to the fine-tuned model (LoRA adapter)
            base_model_name: Name of the base model (if not saved with adapter)
        """
        print("Loading Kira Health Assistant...")
        
        # Determine device
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {self.device}")
        
        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        
        # Load model
        if base_model_name:
            # Load base model and adapter separately
            print(f"Loading base model: {base_model_name}")
            base_model = AutoModelForCausalLM.from_pretrained(
                base_model_name,
                device_map="auto",
                torch_dtype=torch.float16
            )
            print(f"Loading LoRA adapter from: {model_path}")
            self.model = PeftModel.from_pretrained(base_model, model_path)
        else:
            # Load complete model
            print(f"Loading model from: {model_path}")
            self.model = AutoModelForCausalLM.from_pretrained(
                model_path,
                device_map="auto",
                torch_dtype=torch.float16
            )
        
        self.model.eval()
        print("✅ Kira is ready!\n")
    
    def generate(
        self,
        user_message: str,
        max_new_tokens: int = 400,
        temperature: float = 0.7,
        top_p: float = 0.9,
        top_k: int = 50,
        repetition_penalty: float = 1.1
    ) -> str:
        """
        Generate a response to a user message.
        
        Args:
            user_message: The user's question or message
            max_new_tokens: Maximum tokens to generate
            temperature: Sampling temperature (higher = more random)
            top_p: Nucleus sampling threshold
            top_k: Top-k sampling
            repetition_penalty: Penalty for repetition
            
        Returns:
            Generated response text
        """
        # Format prompt
        prompt = f"""<|system|>
You are Kira, a knowledgeable medical assistant. Provide accurate, helpful information about medical topics.</|system|>
<|user|>
{user_message}</|user|>
<|assistant|>
"""
        
        # Tokenize
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        
        # Generate
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                do_sample=True,
                repetition_penalty=repetition_penalty,
                pad_token_id=self.tokenizer.eos_token_id
            )
        
        # Decode
        full_response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extract assistant's response
        if '<|assistant|>' in full_response:
            response = full_response.split('<|assistant|>')[-1].strip()
        else:
            response = full_response
        
        return response
    
    def chat(self):
        """Interactive chat mode."""
        print("=" * 70)
        print("🩺 Kira Health Assistant - Interactive Mode")
        print("=" * 70)
        print("Ask me any medical questions!")
        print("Commands: 'quit' or 'exit' to stop, 'clear' to clear screen")
        print("⚠️  Disclaimer: For educational purposes only. Consult a doctor for medical advice.")
        print("=" * 70)
        print()
        
        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                # Check for commands
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("\n👋 Thank you for using Kira Health Assistant!")
                    break
                
                if user_input.lower() == 'clear':
                    import os
                    os.system('clear' if os.name != 'nt' else 'cls')
                    continue
                
                # Generate response
                print("\nKira: ", end="", flush=True)
                response = self.generate(user_input)
                print(response)
                print("\n" + "-" * 70 + "\n")
                
            except KeyboardInterrupt:
                print("\n\n👋 Thank you for using Kira Health Assistant!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}\n")


def main():
    """Main function for CLI."""
    parser = argparse.ArgumentParser(description="Kira Health Assistant Inference")
    parser.add_argument(
        "--model_path",
        type=str,
        default="./kira_final_model",
        help="Path to the fine-tuned model"
    )
    parser.add_argument(
        "--base_model",
        type=str,
        default=None,
        help="Base model name (if loading adapter separately)"
    )
    parser.add_argument(
        "--question",
        type=str,
        default=None,
        help="Single question to ask (non-interactive mode)"
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="Sampling temperature"
    )
    parser.add_argument(
        "--max_tokens",
        type=int,
        default=400,
        help="Maximum tokens to generate"
    )
    
    args = parser.parse_args()
    
    # Initialize assistant
    assistant = KiraHealthAssistant(
        model_path=args.model_path,
        base_model_name=args.base_model
    )
    
    # Single question mode
    if args.question:
        print(f"Question: {args.question}\n")
        response = assistant.generate(
            args.question,
            max_new_tokens=args.max_tokens,
            temperature=args.temperature
        )
        print(f"Kira: {response}")
    else:
        # Interactive mode
        assistant.chat()


if __name__ == "__main__":
    main()
