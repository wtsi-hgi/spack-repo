# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDownscale(RPackage):
	"""Downscaling Species Occupancy

	Uses species occupancy at coarse grain sizes to predict species occupancy at fine grain sizes. Ten models are provided to fit and extrapolate the occupancy-area relationship, as well as methods for preparing atlas data for modelling. See Marsh et. al. (2018) <doi:10.18637/jss.v086.c03>.
	"""
	
	homepage = "https://github.com/charliem2003/downscale"
	cran = "downscale" 

	version("5.0.0", md5="64344bf310be32eef20de0125dc0f1e5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-cubature@1.1.2:", type=("build", "run"))
	depends_on("r-minpack-lm@1.1.9:", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-sf@1.0.9:", type=("build", "run"))
	depends_on("r-terra@1.7.3:", type=("build", "run"))
