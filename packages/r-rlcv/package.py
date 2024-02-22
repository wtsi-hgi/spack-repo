# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlcv(RPackage):
	"""Robust Likelihood Cross Validation Bandwidth Selection

	Robust likelihood cross validation bandwidth for uni- and multi-variate kernel densities. It is robust against fat-tailed distributions and/or outliers. Based on "Robust Likelihood Cross-Validation for Kernel Density Estimation," Wu (2019) <doi:10.1080/07350015.2018.1424633>.
	"""
	
	homepage = "https://sites.google.com/tamu.edu/ximingwu/"
	cran = "rlcv" 

	version("1.0.0", md5="be78024f74983326cbf6f7b5abbaaf5c")

	depends_on("r-statmod", type=("build", "run"))
