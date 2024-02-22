# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDerivmkts(RPackage):
	"""Functions and R Code to Accompany Derivatives Markets

	A set of pricing and expository functions that should
    be useful in teaching a course on financial derivatives.
	"""
	
	cran = "derivmkts" 

	version("0.2.5", md5="6245a620c90e1c1bd4d4d5a8065bf8e7")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
