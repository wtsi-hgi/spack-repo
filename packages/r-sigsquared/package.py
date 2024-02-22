# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigsquared(RPackage):
	"""Gene signature generation for functionally validated signaling pathways

	By leveraging statistical properties (log-rank test for survival) of patient cohorts defined by binary thresholds, poor-prognosis patients are identified by the sigsquared package via optimization over a cost function reducing type I and II error.
	"""
	
	bioc = "sigsquared" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/sigsquared_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/sigsquared/sigsquared_1.34.0.tar.gz"]

	version("1.34.0", md5="f7dfbb4c066df8fe146b2b73f8180195")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
