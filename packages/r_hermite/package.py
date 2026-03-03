# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHermite(RPackage):
	"""Generalized Hermite Distribution

	Probability functions and other utilities for the generalized Hermite distribution.
	"""
	
	cran = "hermite" 

	version("1.1.2", md5="7cacf65bced01acf4bba62a1e6bb0b49")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
