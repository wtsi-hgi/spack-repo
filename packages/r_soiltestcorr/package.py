# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoiltestcorr(RPackage):
	"""Soil Test Correlation and Calibration

	A compilation of functions designed to assist users on the correlation analysis of crop yield and soil test values. Functions to estimate crop response patterns to soil nutrient availability and critical soil test values using various approaches such as: 1) the modified arcsine-log calibration curve (Correndo et al. (2017) <doi:10.1071/CP16444>); 2) the graphical Cate-Nelson quadrants analysis (Cate & Nelson (1965)), 3) the statistical Cate-Nelson quadrants analysis (Cate & Nelson (1971) <doi:10.2136/sssaj1971.03615995003500040048x>), 4) the linear-plateau regression (Anderson & Nelson (1975) <doi:10.2307/2529422>), 5) the quadratic-plateau regression (Bullock & Bullock (1994) <doi:10.2134/agronj1994.00021962008600010033x>), and 6) the Mitscherlich-type exponential regression (Melsted & Peck (1977) <doi:10.2134/asaspecpub29.c1>). The package development stemmed from ongoing work with the Fertilizer Recommendation Support Tool (FRST) and Feed the Future Innovation Lab for Collaborative Research on Sustainable Intensification (SIIL) projects. 
	"""
	
	homepage = "https://adriancorrendo.github.io/soiltestcorr/"
	cran = "soiltestcorr" 

	version("2.2.0", md5="425188d8c930b9b3fc6d28f9c0661453")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpp", type=("build", "run"))
	depends_on("r-nlstools", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-modelr", type=("build", "run"))
	depends_on("r-nlraa", type=("build", "run"))
	depends_on("r-aiccmodavg", type=("build", "run"))
	depends_on("r-smatr", type=("build", "run"))
