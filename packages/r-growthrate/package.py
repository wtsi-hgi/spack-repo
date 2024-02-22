# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrowthrate(RPackage):
	"""Bayesian reconstruction of growth velocity

	A nonparametric empirical Bayes method for recovering
        gradients (or growth velocities) from observations of smooth
        functions (e.g., growth curves) at isolated time points.
	"""
	
	cran = "growthrate" 

	version("1.3", md5="afed2d8bf632a3d083d33cceb73d4a05")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-clime", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
