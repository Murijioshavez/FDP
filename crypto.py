# Importar las bibliotecas necesarias
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import os
import shutil

# Entrenar el modelo
print("Entrenando el modelo...")
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Asegurarse de que el token de padding es una cadena
if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
tokenizer.pad_token = tokenizer.eos_token if tokenizer.eos_token else '[PAD]'

# Guardar el modelo entrenado
print("Guardando el modelo...")
model.save_pretrained('./my_model')
tokenizer.save_pretrained('./my_model')

# Función para dividir el modelo en shards
def split_model(model_path, num_shards):
    files = os.listdir(model_path)
    shard_size = len(files) // num_shards
    for i in range(num_shards):
        shard_path = f'{model_path}_shard_{i+1}'
        os.makedirs(shard_path, exist_ok=True)
        print(f"Creando shard {i+1} en {shard_path}...")
        for j in range(i * shard_size, (i + 1) * shard_size):
            src_file = os.path.join(model_path, files[j])
            dst_file = os.path.join(shard_path, files[j])
            if os.path.exists(dst_file):
                os.remove(dst_file)  # Eliminar el archivo duplicado si ya existe
            shutil.move(src_file, dst_file)
        print(f"Shard {i+1} completado.")

# Dividir el modelo en tres shards
print("Dividiendo el modelo en shards...")
split_model('./my_model', 3)
print("División completada.")