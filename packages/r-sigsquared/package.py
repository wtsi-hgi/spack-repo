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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sigsquared_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sigsquared/sigsquared_1.34.0.tar.gz"]

	version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="3b58cb88db445f4786a6088c45d7be4264539d3536b2e4befd8ff6076f7e4acb")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
