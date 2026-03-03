# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterpretci(RPackage):
	"""Estimate the Confidence Interval and Interpret Step by Step

	Estimate confidence intervals for mean, proportion, mean difference 
   for unpaired and paired samples and proportion difference. Plot the confidence 
   intervals. Generate documents explaining the statistical result step by step.
	"""
	
	homepage = "https://github.com/cardiomoon/interpretCI"
	cran = "interpretCI" 

	version("0.1.1", md5="fa860e0e6cce538c8cd0892c641a5195")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggbeeswarm", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-aplot", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-english", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-moonbook", type=("build", "run"))
