# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadods(RPackage):
	"""Read and Write ODS Files

	Read ODS (OpenDocument Spreadsheet) into R as data frame. Also support writing data frame into ODS file.
	"""
	
	homepage = "https://github.com/ropensci/readODS"
	cran = "readODS" 

	version("2.2.0", md5="5f1aced02d6d7d3d6d8dbef933d7c425")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cellranger", type=("build", "run"))
	depends_on("r-readr@1.2.1:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs@0.4.2:", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-cpp11@0.4.6:", type=("build", "run"))
