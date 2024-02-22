# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVcdextra(RPackage):
	"""'vcd' Extensions and Additions

	Provides additional data sets, methods and documentation to complement the 'vcd' package for Visualizing Categorical Data
    and the 'gnm' package for Generalized Nonlinear Models.
	In particular, 'vcdExtra' extends mosaic, assoc and sieve plots from 'vcd' to handle 'glm()' and 'gnm()' models and
	adds a 3D version in 'mosaic3d'.  Additionally, methods are provided for comparing and visualizing lists of
	'glm' and 'loglm' objects. This package is now a support package for the book, "Discrete Data Analysis with R" by
  Michael Friendly and David Meyer.
	"""
	
	homepage = "https://friendly.github.io/vcdExtra/"
	cran = "vcdExtra" 

	version("0.8-5", md5="fe0e571d8f30de511394807e653a7611")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
	depends_on("r-gnm@1.0.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ca", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
