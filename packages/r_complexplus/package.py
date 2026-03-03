# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComplexplus(RPackage):
	"""Functions of Complex or Real Variable

	Extension of several functions to the complex domain, including the matrix exponential and logarithm, and the determinant.
	"""
	
	cran = "complexplus" 

	version("2.1", md5="bb19ba38cb8037be0b4250ed856eb854")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-expm@0.999.2:", type=("build", "run"))
	depends_on("r-matrix@1.2.6:", type=("build", "run"))
