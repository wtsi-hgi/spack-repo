# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmat(RPackage):
	"""The Fill-Mask Association Test

	
    The Fill-Mask Association Test ('FMAT')
    is an integrative and probability-based method using
    Masked Language Models to measure conceptual associations
    (e.g., attitudes, biases, stereotypes, social norms, cultural values)
    as propositions in natural language.
    Supported language models include 'BERT'
    <arXiv:1810.04805> and its variants available at 'Hugging Face'
    <https://huggingface.co/models?pipeline_tag=fill-mask>.
    Methodological references and installation guidance are provided at
    <https://psychbruce.github.io/FMAT/>.
	"""
	
	homepage = "https://psychbruce.github.io/FMAT/"
	cran = "FMAT" 

	version("2024.3", md5="b9910c6d1fcdd5239015a1d50776c001")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-psychwordvec", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("python@3.9.0:", type=("build", "link", "run"))
