# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmat(RPackage):
	"""The Fill-Mask Association Test

	
    The Fill-Mask Association Test ('FMAT') is an integrative, versatile,
    and probability-based method that uses Masked Language Models
    to measure conceptual associations or relations
    (e.g., attitudes, biases, stereotypes, social norms, cultural values)
    as propositional representations in natural language.
    The supported language models include
    'BERT' (Devlin et al., 2018) <arXiv:1810.04805>
    and its model variants available at 'Hugging Face'
    <https://huggingface.co/models?pipeline_tag=fill-mask>.
    'Python' ('conda') environment and the 'transformers' module can be
    installed automatically using the FMAT_load() function.
    Methodological references and technical details are provided at
    <https://psychbruce.github.io/FMAT/>.
	"""
	
	homepage = "https://psychbruce.github.io/FMAT/"
	cran = "FMAT" 

	version("2023.8", md5="4048678beb2614e717e211136cacaa25")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-psychwordvec", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-text", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("python", type=("build", "link", "run"))
