# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarcher(RPackage):
	"""Migration and Range Change Estimation in R

	A set of tools for likelihood-based estimation, model selection and testing of two- and three-range shift and migration models for animal movement data as described in Gurarie et al. (2017) <doi: 10.1111/1365-2656.12674>.  Provided movement data (X, Y and Time), including irregularly sampled data, functions estimate the time, duration and location of one or two range shifts, as well as the ranging area and auto-correlation structure of the movment.  Tests assess, for example, whether the shift was "significant", and whether a two-shift migration was a true return migration.
	"""
	
	cran = "marcher" 

	version("0.0-2", md5="3e12b58916f1581fed4782a309f30c22")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
