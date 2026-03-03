# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2roc(RPackage):
	"""AUC Statistics

	Area under the receiver operating characteristic curves (AUC) statistic for significance test. Variance and covariance of AUC values used to assess the 95% Confidence interval (CI) and p-value of the AUC difference for both nested and non-nested model.
	"""
	
	homepage = "https://github.com/mommy003/R2ROC"
	cran = "R2ROC" 

	version("1.0.1", md5="8cf198abfe7f4115f28b1376039dbfcf")

	depends_on("r@2.10:", type=("build", "run"))
