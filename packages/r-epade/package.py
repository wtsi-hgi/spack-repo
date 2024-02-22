# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpade(RPackage):
	"""Easy Plots

	A collection of nice plotting functions directly from a data.frame with limited customisation possibilities.
	"""
	
	cran = "epade" 

	version("0.5.1", md5="43f628ed499cacb8bfce101a6c47f602")

	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
