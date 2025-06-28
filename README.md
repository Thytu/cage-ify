# 🎭 Cage-ify

[![Demo](https://img.shields.io/badge/🚀_Try_It_Live-brightgreen)](https://fal.ai/models/fal-ai/image-editing/cage-ify)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/ThytuVDM.svg?style=social&label=Follow%20%ThytuVDM)](https://twitter.com/ThytuVDM)

> Transform any face into Nicolas Cage's face while maintaining the original expression, lighting, and pose.

## 🎯 What is Cage-ify?

Cage-ify is a custom LoRA fine-tune of FLUX.1 Kontext that can replace any human face with Nicolas Cage's face in ~2 seconds, while preserving the original facial expression, lighting conditions, and head positioning.

### ✨ Key Features

- **🎭 Perfect Face Replacement**: Seamlessly swaps any face with Nicolas Cage
- **⚡ Lightning Fast**: 2-second inference time  
- **🎨 Expression Matching**: Maintains original facial expressions
- **💡 Lighting Preservation**: Keeps original lighting and shadows
- **📐 Pose Retention**: Preserves head position and angle
- **🌍 Universal Compatibility**: Works on any photo with a visible face

## 🚀 Quick Start

### Try Online (Recommended)
[**🎮 Try Cage-ify Live →**](https://fal.ai/models/fal-ai/image-editing/cage-ify)

### API Usage
```python
import fal_client

def cage_ify_image(image_url):
    result = fal_client.submit(
        "fal-ai/flux-kontext-lora",
        arguments={
            "image_url": image_url,
            "prompt": "Transform the face into Nicolas Cage's face",
            "lora_path": "your-lora-path-here"
        }
    )
    return result
```

## 📸 Examples

| Original | Cage-ified | Description |
|----------|------------|-------------|
| ![Original 1](examples/before1.jpg) | ![Caged 1](examples/after1.jpg) | Professional headshot → Professional Cage |
| ![Original 2](examples/before2.jpg) | ![Caged 2](examples/after2.jpg) | Wedding photo → Cage wedding |
| ![Original 3](examples/before3.jpg) | ![Caged 3](examples/after3.jpg) | Family portrait → The Cage family |

## 🛠️ How It Works

### Training Process
1. **Data Collection**: Gathered 100+ high-quality Nicolas Cage images
2. **Reverse Engineering**: Used FLUX.1 Kontext to transform Cage faces into diverse other faces
3. **Dataset Creation**: Flipped the pairs to create "other face → Cage" training data
4. **LoRA Training**: Fine-tuned FLUX.1 Kontext [dev] using the dataset

### Technical Details
- **Base Model**: FLUX.1 Kontext [dev]
- **Training Method**: LoRA (Low-Rank Adaptation)
- **Dataset Size**: 100+ face transformation pairs
- **Training Prompt**: "Transform the face into Nicolas Cage's face, maintaining the original facial expression, lighting, and head position"
- **Inference Time**: ~2 seconds
- **Cost**: $0.025/megapixel

## 🎨 Use Cases

- **🎪 Meme Creation**: The ultimate meme generator
- **🎬 Movie Poster Parodies**: Cage-ify your favorite films
- **👨‍👩‍👧‍👦 Family Photos**: Make everyone in the family Nicolas Cage
- **🎭 Social Media Content**: Viral-ready content creation
- **🎨 Art Projects**: Creative digital art and collages
- **🎉 Party Entertainment**: Hilarious photo booth effects

## 📚 Training Your Own Version

Want to create your own celebrity face-swap model? Here's how:

### 1. Data Collection
```bash
# Collect celebrity images
mkdir dataset
# Download 50-100+ images of your target celebrity
```

### 2. Dataset Creation
```python
# Use FLUX.1 Kontext to create reverse pairs
# Transform celebrity → generic faces
# Then flip for training: generic → celebrity
```

### 3. Training
```bash
# Upload to fal.ai FLUX Kontext trainer
# Set default prompt for transformation
# Train for 500-1000 steps
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

- 🐛 **Report Bugs**: Found a face that won't Cage-ify? Let us know!
- 🎨 **Submit Examples**: Share your best Cage-ified images
- 💡 **Feature Requests**: Ideas for improvements
- 📖 **Documentation**: Help improve our docs

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Black Forest Labs** for creating FLUX.1 Kontext
- **fal.ai** for providing training and inference infrastructure  
- **Nicolas Cage** for being the One True God of faces
- **The Internet** for demanding this exist

## 📞 Contact

- **Twitter**: [@ThytuVDM](https://twitter.com/ThytuVDM)
- **Issues**: [GitHub Issues](https://github.com/Thytu/cage-ify/issues)

---

<div align="center">

**⭐ Star this repo if Cage-ify brought joy to your life! ⭐**

*"I'm gonna steal the Declaration of Independence... and every face on the internet."* - Nicolas Cage (probably)

</div>
