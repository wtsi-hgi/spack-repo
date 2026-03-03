# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCgpfunctions(RPackage):
	"""Powell Miscellaneous Functions for Teaching and Learning
Statistics

	Miscellaneous functions useful for teaching statistics as well as actually practicing the art. They typically are not new methods but rather wrappers around either base R or other packages.
	"""
	
	homepage = "https://github.com/ibecav/CGPfunctions"
	cran = "CGPfunctions" 

	version("0.6.3", md5="dfaf9a961b291cb9726780e5c120cb3b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bayesfactor", type=("build", "run"))
	depends_on("r-desctools@0.99.32:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggmosaic", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-paletteer", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales@1.1:", type=("build", "run"))
	depends_on("r-sjstats@0.17.9:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
