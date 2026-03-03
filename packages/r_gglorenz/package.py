# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGglorenz(RPackage):
	"""Plotting Lorenz Curve with the Blessing of 'ggplot2'

	Provides statistical transformations for plotting empirical 
    ordinary Lorenz curve (Lorenz 1905) <doi:10.2307/2276207> and 
    generalized Lorenz curve (Shorrocks 1983) <doi:10.2307/2554117>.
	"""
	
	homepage = "https://github.com/jjchern/gglorenz"
	cran = "gglorenz" 

	version("0.0.2", md5="1d59dc5939a5f6fbd12a74dcb6c8d048")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-ineq", type=("build", "run"))
