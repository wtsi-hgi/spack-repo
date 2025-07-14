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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CNORfuzzy_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CNORfuzzy/CNORfuzzy_1.44.0.tar.gz"]

	version("1.50.0", tag="RELEASE_3_21")
	version("1.44.0", sha256="07c9b8143fbbe50faa755951c20eb8f7001f652cf95221c4701988880ec870d5")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-cellnoptr@1.4:", type=("build", "run"))
	depends_on("r-nloptr@0.8.5:", type=("build", "run"))
