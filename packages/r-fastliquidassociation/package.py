# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastliquidassociation(RPackage):
	"""functions for genome-wide application of Liquid Association

	This package extends the function of the LiquidAssociation package for genome-wide application. It integrates a screening method into the LA analysis to reduce the number of triplets to be examined for a high LA value and provides code for use in subsequent significance analyses.
	"""
	
	bioc = "fastLiquidAssociation" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/fastLiquidAssociation_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/fastLiquidAssociation/fastLiquidAssociation_1.38.0.tar.gz"]

	version("1.38.0", md5="b57e0af4700d6a6872d88ca0d2eda5d1")

	depends_on("r-liquidassociation", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
