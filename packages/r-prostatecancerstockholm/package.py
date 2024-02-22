# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProstatecancerstockholm(RPackage):
	"""Prostate Cancer Data

	A Bioconductor data package for the Stockholm dataset
	"""
	
	bioc = "prostateCancerStockholm" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/prostateCancerStockholm_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/prostateCancerStockholm/prostateCancerStockholm_1.30.0.tar.gz"]

	version("1.30.0", md5="49326bf3b6f66be78fa1e6d6768b5538")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r@3.3:", type=("build", "run"))

	# experiment