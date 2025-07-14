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

	version("1.40.0", commit="b787191b90181ee40fb13c4d45a9252b9ab764a8")
	version("1.34.0", commit="ca8d23e9f1ff91e4a35977720ac0e2c608064adc")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
