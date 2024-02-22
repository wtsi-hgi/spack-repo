# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcurvep(RPackage):
	"""Concentration-Response Data Analysis using Curvep

	An R interface for processing concentration-response datasets using Curvep, a response noise filtering algorithm. The algorithm was described in the publications (Sedykh A et al. (2011) <doi:10.1289/ehp.1002476> and Sedykh A (2016) <doi:10.1007/978-1-4939-6346-1_14>). Other parametric fitting approaches (e.g., Hill equation) are also adopted for ease of comparison. 3-parameter Hill equation from 'tcpl' package (Filer D et al.,  <doi:10.1093/bioinformatics/btw680>) and 4-parameter Hill equation from Curve Class2 approach (Wang Y et al.,  <doi:10.2174/1875397301004010057>) are available. Also, methods for calculating the confidence interval around the activity metrics are also provided. The methods are based on the bootstrap approach to simulate the datasets (Hsieh J-H et al. <doi:10.1093/toxsci/kfy258>). The simulated datasets can be used to derive the baseline noise threshold in an assay endpoint. This threshold is critical in the toxicological studies to derive the point-of-departure (POD).
	"""
	
	homepage = "https://github.com/moggces/Rcurvep"
	cran = "Rcurvep" 

	version("1.3.1", md5="e9bced9848005c43f184d1a8b9028ef1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("openjdk", type=("build", "link", "run"))
