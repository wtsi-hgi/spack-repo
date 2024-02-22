# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RText(RPackage):
	"""Analyses of Text using Transformers Models from HuggingFace,
Natural Language Processing and Machine Learning

	Link R with Transformers from Hugging Face to transform text variables to word embeddings; where the word embeddings are used to statistically test the mean difference between set of texts, compute semantic similarity scores between texts, predict numerical variables, and visual statistically significant words according to various dimensions etc. For more information see  <https://www.r-text.org>.
	"""
	
	homepage = "https://r-text.org/"
	cran = "text" 

	version("1.2.0", md5="c53644e7ae5fc0386c3bb023a812613a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-parsnip", type=("build", "run"))
	depends_on("r-recipes@0.1.16:", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-tune", type=("build", "run"))
	depends_on("r-workflows", type=("build", "run"))
	depends_on("r-yardstick", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-overlapping", type=("build", "run"))
	depends_on("python", type=("build", "link", "run"))
