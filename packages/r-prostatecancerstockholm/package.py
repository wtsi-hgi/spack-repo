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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/prostateCancerStockholm_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/prostateCancerStockholm/prostateCancerStockholm_1.30.0.tar.gz"]

	version("1.30.0", sha256="49250bdbe02e2c9bd5fcd78290719da3207fdd57512ae8bccc4cf29c57e8b3a5")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r@3.3:", type=("build", "run"))

