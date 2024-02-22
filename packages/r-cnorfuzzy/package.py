# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnorfuzzy(RPackage):
	"""Addon to CellNOptR: Fuzzy Logic

	This package is an extension to CellNOptR.  It contains additional functionality needed to simulate and train a prior knowledge network to experimental data using constrained fuzzy logic (cFL, rather than Boolean logic as is the case in CellNOptR).  Additionally, this package will contain functions to use for the compilation of multiple optimization results (either Boolean or cFL).
	"""
	
	bioc = "CNORfuzzy" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CNORfuzzy_1.44.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CNORfuzzy/CNORfuzzy_1.44.0.tar.gz"]

	version("1.44.0", md5="c7d388f25498f45c39d8af83c5e14a89")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-cellnoptr@1.4:", type=("build", "run"))
	depends_on("r-nloptr@0.8.5:", type=("build", "run"))
