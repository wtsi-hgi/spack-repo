# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHarmonizr(RPackage):
	"""Handles missing values and makes more data available

	An implementation, which takes input data and makes it available for proper batch effect removal by ComBat or Limma. The implementation appropriately handles missing values by dissecting the input matrix into smaller matrices with sufficient data to feed the ComBat or limma algorithm. The adjusted data is returned to the user as a rebuild matrix. The implementation is meant to make as much data available as possible with minimal data loss.
	"""
	
	bioc = "HarmonizR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/HarmonizR_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/HarmonizR/HarmonizR_1.0.0.tar.gz"]

	version("1.0.0", sha256="9226855ffafdcbdedb160b454e31faa2d368646d90b6c8975ae19ac973c44fbf")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-doparallel@1.0.16:", type=("build", "run"))
	depends_on("r-foreach@1.5.1:", type=("build", "run"))
	depends_on("r-janitor@2.1:", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-sva@3.36:", type=("build", "run"))
	depends_on("r-seriation@1.3.5:", type=("build", "run"))
	depends_on("r-limma@3.46:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
