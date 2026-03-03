# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlpred(RPackage):
	"""Estimators of Non-Linear Cross-Validated Risks Optimized for
Small Samples

	Methods for obtaining improved estimates of non-linear cross-validated risks are obtained using targeted minimum loss-based estimation, estimating equations, and one-step estimation (Benkeser, Petersen, van der Laan (2019), <doi:10.1080/01621459.2019.1668794>). Cross-validated area under the receiver operating characteristics curve (LeDell, Petersen, van der Laan (2015), <doi:10.1214/15-EJS1035>) and other metrics are included.
	"""
	
	cran = "nlpred" 

	version("1.0.1", md5="881eb9979c1ce2069703db84710e993c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-cvauc", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-bde", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
