# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdmur(RPackage):
	"""Ancient Demographic Modelling Using Radiocarbon

	Provides tools to directly model underlying population dynamics using date datasets (radiocarbon and other) with a Continuous Piecewise Linear (CPL) model framework. Various other model types included. Taphonomic loss included optionally as a power function. Model comparison framework using BIC. Package also calibrates 14C samples, generates Summed Probability Distributions (SPD), and performs SPD simulation analysis to generate a Goodness-of-fit test for the best selected model. Details about the method can be found in Timpson A., Barberena R., Thomas M. G., Mendez C., Manning K. (2020) <doi:10.1098/rstb.2019.0723>.
	"""
	
	homepage = "https://github.com/UCL/ADMUR"
	cran = "ADMUR" 

	version("1.0.3", md5="1c1c5b1f26ea8ecce092424323e7ab95")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
