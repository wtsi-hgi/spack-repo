# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCutpointr(RPackage):
	"""Determine and Evaluate Optimal Cutpoints in Binary
Classification Tasks

	Estimate cutpoints that optimize a specified metric in binary classification tasks
    and validate performance using bootstrapping. Some methods for more robust cutpoint
    estimation are supported, e.g. a parametric method assuming normal distributions,
    bootstrapped cutpoints, and smoothing of the metric values per cutpoint using
    Generalized Additive Models. Various plotting functions are included. For an overview
    of the package see Thiele and Hirschfeld (2021) <doi:10.18637/jss.v098.i11>.
	"""
	
	homepage = "https://github.com/thie1e/cutpointr"
	cran = "cutpointr" 

	version("1.1.2", md5="8d293ff620ac93aee7ec2efe5358fa87")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gridextra@2.2.1:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
