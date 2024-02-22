# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSse(RPackage):
	"""Sample Size Estimation

	Provides functions to evaluate user-defined power functions for a parameter range, and draws a sensitivity plot. It also provides a resampling procedure for semi-parametric sample size estimation and methods for adding information to a Sweave report.
	"""
	
	homepage = "http://r-forge.r-project.org/projects/power/"
	cran = "sse" 

	version("0.7-17", md5="daa6f8abbfc8aeeed0e8f1751d6455d9")

	depends_on("r-lattice", type=("build", "run"))
