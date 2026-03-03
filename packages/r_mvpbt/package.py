# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvpbt(RPackage):
	"""Publication Bias Tests for Meta-Analysis of Diagnostic Accuracy
Test

	Generalized Egger tests for detecting publication bias in meta-analysis for diagnostic accuracy test (Noma (2020) <doi:10.1111/biom.13343>, Noma (2022) <doi:10.48550/arXiv.2209.07270>). These publication bias tests are generally more powerful compared with the conventional univariate publication bias tests and can incorporate correlation information between the outcome variables.   
	"""
	
	cran = "MVPBT" 

	version("1.2-1", md5="34fc3bcc90854fde03216a5e78328a99")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-mada", type=("build", "run"))
	depends_on("r-mvmeta", type=("build", "run"))
