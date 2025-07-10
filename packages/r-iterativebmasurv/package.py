# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIterativebmasurv(RPackage):
	"""The Iterative Bayesian Model Averaging (BMA) Algorithm For Survival Analysis

	The iterative Bayesian Model Averaging (BMA) algorithm for survival analysis is a variable selection method for applying survival analysis to microarray data.
	"""
	
	homepage = "http://expression.washington.edu/ibmasurv/protected"
	bioc = "iterativeBMAsurv" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iterativeBMAsurv_1.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iterativeBMAsurv/iterativeBMAsurv_1.60.0.tar.gz"]

	version("1.60.0", sha256="09e9a010a303c25c85540bc32e768173f4dda11980b3ae5ff9347e2a10fa93c4")

	depends_on("r-bma", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
