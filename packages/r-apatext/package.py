# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApatext(RPackage):
	"""Create R Markdown Text for Results in the Style of the American
Psychological Association (APA)

	Create APA style text from analyses for use within R Markdown documents. Descriptive statistics, confidence intervals, and cell sizes are reported.
	"""
	
	cran = "apaText" 

	version("0.1.7", md5="8f2c42dad5cf5ad59844da7ceeeb2388")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-cocor", type=("build", "run"))
