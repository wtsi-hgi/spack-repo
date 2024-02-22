# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSap(RPackage):
	"""Statistical Analysis and Programming

	The Hypothesis tests for the means of independent or paired groups.
    This package investigates the normality assumption automatically.
    Then, it tests the hypothesis tests for two independent or paired group means
    by using parametric or non-parametric tests. It uses the Shapiro-Wilk test to
    test the normality assumption. For independent two groups, If data comes from
    the normal distribution, the package uses the Z or t-test according to whether
    variances are known. For paired groups, it uses paired t-test under normal data
    sets. If data does not come from the normal distribution, the package uses the
    Wilcoxon test for independent and paired cases.
	"""
	
	cran = "SAP" 

	version("1.0", md5="6c9ff10cf0c00dbdedc0d24dea806f3a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bsda", type=("build", "run"))
