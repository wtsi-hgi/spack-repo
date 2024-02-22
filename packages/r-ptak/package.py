# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtak(RPackage):
	"""Principal Tensor Analysis on k Modes

	A multiway method to decompose a tensor (array) of any order, as a generalisation of SVD also supporting non-identity metrics and penalisations. 2-way SVD with these extensions is also available. The package includes also some other multiway methods: PCAn (Tucker-n) and PARAFAC/CANDECOMP with these extensions. 
	"""
	
	homepage = "https://www.GeotRYcs.com"
	cran = "PTAk" 

	version("2.0.0", md5="067c48d3ea2bbc2499fe4ec1c51ef04a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tensor", type=("build", "run"))
