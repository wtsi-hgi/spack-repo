# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmenet(RPackage):
	"""Bi-Level Selection of Conditional Main Effects

	Provides functions for implementing cmenet - a bi-level variable selection method for conditional main effects (see Mak and Wu (2018) <doi:10.1080/01621459.2018.1448828>). CMEs are reparametrized interaction effects which capture the conditional impact of a factor at a fixed level of another factor. Compared to traditional two-factor interactions, CMEs can quantify more interpretable interaction effects in many problems. The current implementation performs variable selection on only binary CMEs; we are working on an extension for the continuous setting.
	"""
	
	cran = "cmenet" 

	version("0.1.2", md5="849ba85b671fc3ca4b49fd22f1a300b1")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-hiernet", type=("build", "run"))
	depends_on("r-sparsenet", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
