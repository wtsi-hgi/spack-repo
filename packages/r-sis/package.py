# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSis(RPackage):
	"""Sure Independence Screening

	Variable selection techniques are essential tools for model
    selection and estimation in high-dimensional statistical models. Through this
    publicly available package, we provide a unified environment to carry out
    variable selection using iterative sure independence screening (SIS) (Fan and Lv (2008)<doi:10.1111/j.1467-9868.2008.00674.x>) and all
    of its variants in generalized linear models (Fan and Song (2009)<doi:10.1214/10-AOS798>) and the Cox proportional hazards
    model (Fan, Feng and Wu (2010)<doi:10.1214/10-IMSCOLL606>).
	"""
	
	cran = "SIS" 

	version("0.8-8", md5="d36c01251e4faea41403fee895a036ce")

	depends_on("r@3.2.4:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
