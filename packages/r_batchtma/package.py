# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBatchtma(RPackage):
	"""Batch Effect Adjustments

	Different adjustment methods for batch effects in biomarker data,
  such as from tissue microarrays. Some methods attempt to retain differences 
  between batches that may be due to between-batch differences in "biological"
  factors that influence biomarker values.
	"""
	
	homepage = "https://stopsack.github.io/batchtma/"
	cran = "batchtma" 

	version("0.1.6", md5="de12f9ca2dec36ad081b42b94f6f7071")

	depends_on("r-broom@0.7:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
