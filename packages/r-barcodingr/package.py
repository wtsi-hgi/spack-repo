# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBarcodingr(RPackage):
	"""Species Identification using DNA Barcodes

	To perform species identification using DNA barcodes.
	"""
	
	cran = "BarcodingR" 

	version("1.0-3", md5="9bdb0ecc5cfc63d85cb929162ac28843")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
