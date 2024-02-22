# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGifi(RPackage):
	"""Multivariate Analysis with Optimal Scaling

	Implements categorical principal component analysis ('PRINCALS'), multiple correspondence analysis ('HOMALS'), monotone regression analysis ('MORALS'). It replaces the 'homals' package. 
	"""
	
	homepage = "https://r-forge.r-project.org/projects/psychor/"
	cran = "Gifi" 

	version("0.4-0", md5="0ea5fd4300f1946510632da5c6e33633")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
