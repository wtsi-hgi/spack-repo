# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNormalp(RPackage):
	"""Routines for Exponential Power Distribution

	A collection of utilities referred to Exponential Power distribution, also known as General Error Distribution (see Mineo, A.M. and Ruggieri, M. (2005), A software Tool for the Exponential Power Distribution: The normalp package. In Journal of Statistical Software, Vol. 12, Issue 4).
	"""
	
	homepage = "https://www.r-project.org"
	cran = "normalp" 

	version("0.7.2.1", md5="74f79caecdc89c86a28396ca33b1e353")

	depends_on("r@1.5:", type=("build", "run"))
