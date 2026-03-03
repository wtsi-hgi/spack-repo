# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGptzeror(RPackage):
	"""Identify Text Written by Large Language Models using 'GPTZero'

	An R interface to the 'GPTZero' API (<https://gptzero.me/docs>). Allows 
    users to classify text into human and computer written with probabilities. Formats
    the data into data frames where each sentence is an observation. Paragraph-level
    and document-level predictions are organized to align with the sentences.
	"""
	
	homepage = "https://github.com/christopherkenny/gptzeror"
	cran = "gptzeror" 

	version("0.0.1", md5="c072336dce6b5eb4ec1c9fd36d1014a4")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
