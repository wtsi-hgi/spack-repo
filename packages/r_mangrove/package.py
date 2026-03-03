# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMangrove(RPackage):
	"""Risk Prediction on Trees

	Methods for performing genetic risk
        prediction from genotype data.  You can use it to perform risk
        prediction for individuals, or for families with missing data.
	"""
	
	cran = "Mangrove" 

	version("1.21", md5="005894f3fe370bbe3d9f924d63227ae2")

	depends_on("r@2.10:", type=("build", "run"))
