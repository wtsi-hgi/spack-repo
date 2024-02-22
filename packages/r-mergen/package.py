# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMergen(RPackage):
	"""AI-Driven Code Generation, Explanation and Execution for Data
Analysis

	Employing artificial intelligence to convert data analysis questions into executable code, explanations, and algorithms. The self-correction feature ensures the generated code is optimized for performance and accuracy. 'mergen' features a user-friendly chat interface, enabling users to interact with the AI agent and extract valuable insights from their data effortlessly.
	"""
	
	cran = "mergen" 

	version("0.1.0", md5="830097813b58f82abe06f225c0c979df")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-openai", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
