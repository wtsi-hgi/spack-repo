# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoxerr(RPackage):
	"""Cox Regression with Dependent Error in Covariates

	Perform the functional modeling methods of Huang and Wang (2018) <doi:10.1111/biom.12741> to accommodate dependent error in covariates of the proportional hazards model. The adopted measurement error model has minimal assumptions on the dependence structure, and an instrumental variable is supposed to be available.
	"""
	
	cran = "coxerr" 

	version("1.1", md5="2fd5d58eeee6d9c75f47ef80f6326a6f")

	depends_on("r@2.8:", type=("build", "run"))
