# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeird(RPackage):
	"""Functions and Data Sets for "That's Weird: Anomaly Detection
Using R" by Rob J Hyndman

	All functions and data sets required for the examples in the book
    Hyndman (2024) "That's Weird: Anomaly Detection Using R" <https://OTexts.com/weird/>.  
    All packages needed to run the examples are also loaded.
	"""
	
	homepage = "https://pkg.robjhyndman.com/weird-package/"
	cran = "weird" 

	version("1.0.2", md5="f99dceb4ae1cf65f91d799ac14b159e7")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-aplpack", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-cli@1:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-interpolation", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-rstudioapi@0.7:", type=("build", "run"))
	depends_on("r-stray", type=("build", "run"))
	depends_on("r-tibble@1.4.2:", type=("build", "run"))
