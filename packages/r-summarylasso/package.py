# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSummarylasso(RPackage):
	"""Building Polygenic Risk Score Using GWAS Summary Statistics

	Shrinkage estimator for polygenic risk prediction models based on summary statistics of genome-wide association studies.
	"""
	
	cran = "SummaryLasso" 

	version("1.2.1", md5="1795c3c68c4cab8172104390f3f810d8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
