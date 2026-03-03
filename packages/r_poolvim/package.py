# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoolvim(RPackage):
	"""Gene-Based Association Tests using the Actual Impurity Reduction
(AIR) Variable Importance

	Gene-based association tests using the actual impurity reduction (AIR) variable importance. The function aggregates AIR importance measures from a group of SNPs or probes and outputs a p-value for each gene. The procedures builds upon the method described in <doi:10.1093/Bioinformatics/Bty373> and will be published soon.
	"""
	
	cran = "poolVIM" 

	version("1.0.0", md5="ba174330cda7c53ea361798125eda190")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-empiricalbrownsmethod@1.6:", type=("build", "run"))
	depends_on("r-hmisc@4.1:", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
