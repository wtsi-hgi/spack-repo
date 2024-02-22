# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModeest(RPackage):
	"""Mode Estimation

	Provides estimators of the mode of univariate
    data or univariate distributions. 
	"""
	
	homepage = "https://github.com/paulponcet/modeest"
	cran = "modeest" 

	version("2.4.0", md5="403dfa0b63b07db8e1856f401ab1a85b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-stable", type=("build", "run"))
	depends_on("r-stabledist", type=("build", "run"))
	depends_on("r-statip@0.2.3:", type=("build", "run"))
