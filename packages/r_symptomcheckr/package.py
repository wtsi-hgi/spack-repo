# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSymptomcheckr(RPackage):
	"""Analyzing and Visualizing Symptom Checker Performance

	Easily analyze and visualize the performance of symptom
    checkers. This package can be used to gain comprehensive insights into
    the performance of single symptom checkers or the performance of
    multiple symptom checkers. It can be used to easily compare these
    symptom checkers across several metrics to gain an understanding of
    their strengths and weaknesses. The metrics are developed in 
    Kopka et al. (2023) <doi:10.1177/20552076231194929>.
	"""
	
	homepage = "https://github.com/ma-kopka/symptomcheckR"
	cran = "symptomcheckR" 

	version("0.1.1", md5="28c2f270284c939af66c556a4e484562")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-ggpubr@0.6:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
