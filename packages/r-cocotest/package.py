# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCocotest(RPackage):
	"""Dependence Condition Test Using Ranked Correlation Coefficients

	A common misconception is that the Hochberg procedure comes up with adequate overall type I error control when test statistics are positively correlated. However, unless the test statistics follow some standard distributions, the Hochberg procedure requires a more stringent positive dependence assumption, beyond mere positive correlation, to ensure valid overall type I error control. To fill this gap, we formulate statistical tests grounded in rank correlation coefficients to validate fulfillment of the positive dependence through stochastic ordering (PDS) condition.
    See Gou, J., Wu, K. and Chen, O. Y. (2024). Rank correlation coefficient based tests on positive dependence through stochastic ordering with application in cancer studies, Technical Report.
	"""
	
	cran = "cocotest" 

	version("1.0.3", md5="88c55b037b66172ef37c4edf40a8ba69")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-boot@1.1:", type=("build", "run"))
