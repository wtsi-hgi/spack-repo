# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJaccard(RPackage):
	"""Test Similarity Between Binary Data using Jaccard/Tanimoto
Coefficients

	Calculate statistical significance of Jaccard/Tanimoto similarity
    coefficients for binary data.
	"""
	
	cran = "jaccard" 

	version("0.1.0", md5="43a45f9bfc343fa03458fc63fda33bc6")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
