# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRapidopgs(RPackage):
	"""A Fast and Light Package to Compute Polygenic Risk Scores

	Quickly computes polygenic scores from GWAS summary statistics of either case-control or quantitative traits without parameter tuning. Reales,G., Vigorito, E., Kelemen,M., Wallace,C. (2021) <doi:10.1101/2020.07.24.220392> "RápidoPGS: A rapid polygenic score calculator for summary GWAS data without a test dataset".
	"""
	
	cran = "RapidoPGS" 

	version("2.3.0", md5="cb576f997aeb6bb7e0f65493307ce031")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr@1.1.3:", type=("build", "run"))
	depends_on("r-genomicranges@1.52:", type=("build", "run"))
	depends_on("r-iranges@2.34.1:", type=("build", "run"))
	depends_on("r-bigsnpr@1.12.2:", type=("build", "run"))
	depends_on("r-coloc@5.2.3:", type=("build", "run"))
	depends_on("r-bigreadr@0.2.5:", type=("build", "run"))
