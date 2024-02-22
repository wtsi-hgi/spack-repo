# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCa3variants(RPackage):
	"""Three-Way Correspondence Analysis Variants

	Provides four variants of three-way correspondence analysis (ca):
 three-way symmetrical ca, three-way non-symmetrical ca, three-way ordered symmetrical ca
 and three-way ordered non-symmetrical ca.
	"""
	
	homepage = "https://www.R-project.org"
	cran = "CA3variants" 

	version("3.3.1", md5="19c8c80be6b1f2ee47e07ce913fa363e")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-multichull", type=("build", "run"))
