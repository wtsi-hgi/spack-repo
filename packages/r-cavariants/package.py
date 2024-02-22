# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCavariants(RPackage):
	"""Correspondence Analysis Variants

	Provides six variants of two-way correspondence analysis (ca):
   simple ca, singly ordered ca, doubly ordered ca, non symmetrical ca,
   singly ordered non symmetrical ca, and doubly ordered non symmetrical
   ca.
	"""
	
	homepage = "https://www.R-project.org"
	cran = "CAvariants" 

	version("6.0", md5="9a6003b1ce3803fcfe3cb58df2b324ee")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
