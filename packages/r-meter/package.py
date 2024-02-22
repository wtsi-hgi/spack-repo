# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeter(RPackage):
	"""Fitting and Plotting Tools for the Maximum Entropy Theory of
Ecology (METE)

	Fit and plot macroecological patterns predicted by the Maximum
    Entropy Theory of Ecology (METE).
	"""
	
	homepage = "https://github.com/cmerow/meteR"
	cran = "meteR" 

	version("1.2", md5="f337cca6c2681cf3c78d10a2d035fd00")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-distr", type=("build", "run"))
