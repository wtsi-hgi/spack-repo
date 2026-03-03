# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQrank(RPackage):
	"""A Novel Quantile Regression Approach for eQTL Discovery

	A Quantile Rank-score based test for the identification of expression quantitative trait loci.
	"""
	
	cran = "QRank" 

	version("1.0", md5="6bddb47d2f53381b44de56e051f8ba59")

	depends_on("r-quantreg", type=("build", "run"))
