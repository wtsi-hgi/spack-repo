# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrspgx(RPackage):
	"""Construct PGx PRS

	Construct pharmacogenomics (PGx) polygenic risk score (PRS) with PRS-PGx-Unadj (unadjusted), PRS-PGx-CT (clumping and thresholding), PRS-PGx-L, -GL, -SGL (penalized regression), PRS-PGx-Bayes (Bayesian regression). Package is based on ''Pharmacogenomics Polyenic Risk Score for Drug Response Prediction Using PRS-PGx Methods'' by Zhai, S., Zhang, H., Mehrotra, D.V., and Shen, J., 2021 (submitted).
	"""
	
	cran = "PRSPGx" 

	version("0.3.0", md5="0fedd877eb3caa43b839cf493f8e8736")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-gglasso@1.5:", type=("build", "run"))
	depends_on("r-sgl@1.3:", type=("build", "run"))
	depends_on("r-glmnet@4.0.2:", type=("build", "run"))
	depends_on("r-bigsnpr@1.5.2:", type=("build", "run"))
	depends_on("r-matrix@1.2.18:", type=("build", "run"))
	depends_on("r-gigrvg@0.5:", type=("build", "run"))
	depends_on("r-mcmcpack@1.4.6:", type=("build", "run"))
	depends_on("r-bdsmatrix@1.3.4:", type=("build", "run"))
	depends_on("r-bigsparser@0.4:", type=("build", "run"))
	depends_on("r-lmtest@0.9.37:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1:", type=("build", "run"))
	depends_on("r-propagate@1.0.6:", type=("build", "run"))
	depends_on("r-bigparallelr@0.2.3:", type=("build", "run"))
	depends_on("r-bigstatsr@1.2.3:", type=("build", "run"))
	depends_on("r-rfast@1.9.9:", type=("build", "run"))
	depends_on("r-matrixcalc@1.0.3:", type=("build", "run"))
