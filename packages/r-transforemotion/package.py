# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransforemotion(RPackage):
	"""Sentiment Analysis for Text, Image and Video using Transformer
Models

	Implements sentiment analysis using huggingface <https://huggingface.co> transformer zero-shot classification model pipelines for text and image data. The default text pipeline is Cross-Encoder's DistilRoBERTa <https://huggingface.co/cross-encoder/nli-distilroberta-base> and default image/video pipeline is Open AI's CLIP  <https://huggingface.co/openai/clip-vit-base-patch32>. All other zero-shot classification model pipelines can be implemented using their model name from <https://huggingface.co/models?pipeline_tag=zero-shot-classification>.
	"""
	
	cran = "transforEmotion" 

	version("0.1.4", md5="8bbe73054e985d0e41b725dae35d9065")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-googledrive", type=("build", "run"))
	depends_on("r-lsafun", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
