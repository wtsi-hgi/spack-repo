# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdwd(RPackage):
	"""Sparse Distance Weighted Discrimination

	Formulates a sparse distance weighted discrimination (SDWD) for high-dimensional classification and implements a very fast algorithm for computing its solution path with the L1, the elastic-net, and the adaptive elastic-net penalties. More details about the methodology SDWD is seen on Wang and Zou (2016) (<doi:10.1080/10618600.2015.1049700>).
	"""
	
	cran = "sdwd" 

	version("1.0.5", md5="40c9997fa149e17f2543be3575920595")

	depends_on("r-matrix", type=("build", "run"))
