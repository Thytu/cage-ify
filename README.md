# 🎭 Cage-ify

[![Demo](https://img.shields.io/badge/🚀_Try_It_Live-brightgreen)](https://fal.ai/models/fal-ai/image-editing/cage-ify)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/ThytuVDM.svg?style=social&label=Follow%20%ThytuVDM)](https://twitter.com/ThytuVDM)

> Transform any face into Nicolas Cage's face while maintaining the original expression, lighting, and pose.

## 🎯 What is Cage-ify?

Cage-ify is a custom LoRA fine-tune of FLUX.1 Kontext that can replace any human face with Nicolas Cage's face while preserving the original facial expression, lighting conditions, and head positioning.

### ✨ Key Features

- **🎭 Perfect Face Replacement**: Seamlessly swaps any face with Nicolas Cage
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

<div align="center">
  <table>
    <tbody>
      <tr>
        <td colspan="2" align="center">Presidential headshot → President Cage</td>
      </tr>
      <tr>
        <td align="center">
          <img src="https://res.cloudinary.com/aenetworks/image/upload/c_fill,ar_2,w_3840,h_1920,g_auto/dpr_auto/f_auto/q_auto:eco/v1/gettyimages-71856793?_a=BAVAZGDX0s" alt="Original presidential headshot" width="400">
        </td>
        <td align="center">
          <img src="https://i.postimg.cc/t4N4TQfp/HBef-Bm8i-IFc-H-IMcipi0.png" alt="Caged presidential headshot" width="400">
        </td>
      </tr>
      <tr>
        <td colspan="2" align="center" style="padding-top: 1.5em;">Family portrait → The Cage family</td>
      </tr>
      <tr>
        <td align="center">
          <img src="https://freedphoto.com/wp-content/uploads/05_Freed_FamilyPortraits.png" alt="Original family portrait" width="400">
        </td>
        <td align="center">
          <img src="https://i.postimg.cc/YSX26NMP/c-O-q-Vn-U-o79-Zo94-LMy-F2w.png" alt="Caged family portrait" width="400">
        </td>
      </tr>
      <tr>
        <td colspan="2" align="center" style="padding-top: 1.5em;">Mount Rushmore → Mount Cagemore</td>
      </tr>
      <tr>
        <td align="center">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Mount_Rushmore_detail_view_%28100MP%29.jpg/1200px-Mount_Rushmore_detail_view_%28100MP%29.jpg" alt="Mount Rushmore" width="400">
        </td>
        <td align="center">
          <img src="https://i.postimg.cc/RVf0knL3/ki-b-Y-sew-ZCIAp-Jg-DYQv.png" alt="Mount Cagemore" width="400">
        </td>
      </tr>
      <tr>
        <td colspan="2" align="center" style="padding-top: 1.5em;">Happy Potter → The Boy Who Caged</td>
      </tr>
      <tr>
        <td align="center">
          <img src="https://occ-0-8407-90.1.nflxso.net/dnm/api/v6/Z-WHgqd_TeJxSuha8aZ5WpyLcX8/AAAABU4M_0ouMw3it5QsXKVM0cS1iy97W8b8ihAihbk0nvfNYRMcGqC1atGJOf_F7vWcI7pA8rMfhNDuaTL4KpxacKqzCU5faUF9EWl7.jpg?r=b7d" alt="Harry Potter" width="400">
        </td>
        <td align="center">
          <img src="https://i.postimg.cc/W4pbqYLr/8-Vj-JQRIuk6h-OKd-VSRQHa-N.png" alt="Harry Potter Caged" width="400">
        </td>
      </tr>
      <tr>
        <td colspan="2" align="center" style="padding-top: 1.5em;">Uncle Sam → Uncle Cage</td>
      </tr>
      <tr>
        <td align="center">
          <img src="https://v3.fal.media/files/rabbit/cJwSIu1EIZVPMngY8-ljg_you-w-background.png" alt="Original Uncle Sam" width="400">
        </td>
        <td align="center">
          <img src="https://i.postimg.cc/x12dnT66/le-Lq1-Dkeopjj-Kybaq-KY2.png" alt="Caged Uncle Sam" width="400">
        </td>
      </tr>
    </tbody>
  </table>
</div>

## 🛠️ How It Works

### Training Process
1. **Data Collection**: Gathered 100+ high-quality Nicolas Cage images
2. **Reverse Engineering**: Used FLUX.1 Kontext to transform Cage faces into diverse other faces
3. **Dataset Creation**: Flipped the pairs to create "other face → Cage" training data
4. **LoRA Training**: Fine-tuned FLUX.1 Kontext [dev] using the dataset

## 🎨 Use Cases

If you really need a reason to why we should Cage-ify everything, here are some:
- **🎬 Movie Poster Parodies**: Cage-ify your favorite films
- **👨‍👩‍👧‍👦 Family Photos**: Make everyone in your family look like Nicolas Cage
- **🎨 Art Projects**: Creative digital art and collages
- **🙏 Our True Leader**: Spray the words


## 📚 Training Your Own Version

Want to create your own version? Here's how:

### 1. Data Collection
```bash
# Collect ~100 Nicolas Cage images
python 0_download_target_images.py
```

### 2. Dataset Creation
```bash
# Use FLUX.1 Kontext to create reverse pairs
# Transform Nicolas Cage → generic faces
# Then flip for training: generic → Nicolas Cage
python 1_generate_image_pairs.py
```

### 3. Training
```bash
# Upload to fal.ai FLUX Kontext trainer
# Set default prompt for transformation
# Train for 1000 steps
python 2_trigger_training
```

### 4. Inference
Wait for your training for finish: https://fal.ai/models/fal-ai/flux-kontext-trainer/requests
Once trained, you can simply click on "Run Inference" and Cage-ify the world.

## 🙏 Acknowledgments

- **Black Forest Labs** for creating FLUX.1 Kontext
- **fal.ai** for providing training and inference infrastructure
- **Nicolas Cage** for being the One True God of faces
- **The Internet** for existing

## 📞 Contact

- **Twitter**: [@ThytuVDM](https://twitter.com/ThytuVDM)
- **Issues**: [GitHub Issues](https://github.com/Thytu/cage-ify/issues)

---

<div align="center">

**⭐ Star this repo if Cage-ify brought joy to your life! ⭐**

*"I'm gonna steal the Declaration of Independence... and every face on the internet."* - Nicolas Cage (probably)

</div>
