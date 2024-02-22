# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVurocs(RPackage):
	"""Volume under the ROC Surface for Multi-Class ROC Analysis

	Calculates the volume under the ROC surface and its (co)variance for ordered multi-class ROC analysis as well as certain bivariate ordinal measures of association.
	"""
	
	cran = "VUROCS" 

	version("1.0", md5="9eff8f858456475a0313ee9f8f653df4")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
