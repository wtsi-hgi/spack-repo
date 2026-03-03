# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwasforest(RPackage):
	"""Make Forest Plot with GWAS Data

	Extract and reform data from GWAS (genome-wide association study) results, and then make a single integrated forest plot containing multiple windows of which each shows the result of individual SNPs (or other items of interest).
	"""
	
	homepage = "https://github.com/yilixu/gwasforest"
	cran = "gwasforest" 

	version("1.0.0", md5="3effa431fff80aa4c42b9cf7268e9f09")

	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
