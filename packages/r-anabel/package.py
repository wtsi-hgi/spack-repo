# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnabel(RPackage):
	"""Analysis of Binding Events + l

	A free software for a fast and easy analysis of 1:1 molecular interaction studies. 
   This package is suitable for a high-throughput data analysis. 
   Both the online app and the package are completely open source. 
   You provide a table of sensogram, tell 'anabel' which method to use,
   and it takes care of all fitting details.
   The first two releases of 'anabel' were created and implemented as in 
   (<doi:10.1177/1177932218821383>, <doi:10.1093/database/baz101>).
	"""
	
	cran = "anabel" 

	version("3.0.1", md5="c83a3a1f3744c4c07ccf0e1f98891f03")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli@3.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-kableextra@1.3:", type=("build", "run"))
	depends_on("r-minpack-lm@1.2:", type=("build", "run"))
	depends_on("r-openxlsx@4.2:", type=("build", "run"))
	depends_on("r-progress@1.2:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
	depends_on("r-reshape2@1.4:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
