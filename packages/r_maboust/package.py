# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaboust(RPackage):
	"""Multi-Armed Bayesian Ordinal Utility-Based Sequential Trial

	Conducts and simulates the MABOUST design, including making interim decisions to stop a treatment for inferiority or stop the trial early for superiority or equivalency.
	"""
	
	cran = "MABOUST" 

	version("1.0.1", md5="1afc3c623654a27b79ad34d81629a363")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
