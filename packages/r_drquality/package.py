# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrquality(RPackage):
	"""Quality Measurements for Dimensionality Reduction

	Several quality measurements for investigating the performance of dimensionality reduction methods are provided here. In addition a new quality measurement called Gabriel classification error is made accessible, which was published in Thrun, M. C., Märte, J., & Stier, Q: "Analyzing Quality Measurements for Dimensionality Reduction" (2023), Machine Learning and Knowledge Extraction (MAKE), <DOI:10.3390/make5030056>.
	"""
	
	cran = "DRquality" 

	version("0.2.1", md5="6cbc21b45850de1d4fdbd0242c0c4a57")

	depends_on("r-databionicswarm", type=("build", "run"))
