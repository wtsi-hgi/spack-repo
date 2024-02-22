# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDevtreatrules(RPackage):
	"""Develop Treatment Rules with Observational Data

	Develop and evaluate treatment rules based on: (1) the standard indirect approach of split-regression, which fits regressions separately in both treatment groups and assigns an individual to the treatment option under which predicted outcome is more desirable; (2) the direct approach of outcome-weighted-learning proposed by Yingqi Zhao, Donglin Zeng, A. John Rush, and Michael Kosorok (2012) <doi:10.1080/01621459.2012.695674>; (3) the direct approach, which we refer to as direct-interactions, proposed by Shuai Chen, Lu Tian, Tianxi Cai, and Menggang Yu (2017) <doi:10.1111/biom.12676>. Please see the vignette for a walk-through of how to start with an observational dataset whose design is understood scientifically and end up with a treatment rule that is trustworthy statistically, along with an estimation of rule benefit in an independent sample.
	"""
	
	cran = "DevTreatRules" 

	version("1.1.0", md5="7b5c7c112f1e2c158abc4107018e63ef")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-dyntxregime", type=("build", "run"))
	depends_on("r-modelobj", type=("build", "run"))
