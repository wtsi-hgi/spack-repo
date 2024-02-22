# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInsurancedata(RPackage):
	"""A Collection of Insurance Datasets Useful in Risk Classification
in Non-life Insurance

	Insurance datasets, which are often used in claims severity and claims frequency modelling. It helps testing new regression models in those problems, such as GLM, GLMM, HGLM, non-linear mixed models etc. Most of the data sets are applied in the project "Mixed models in ratemaking" supported by grant NN 111461540 from Polish National Science Center.    
	"""
	
	cran = "insuranceData" 

	version("1.0", md5="a788183a0a2b3240aa5ba03e8a4013a0")

	depends_on("r@2.10:", type=("build", "run"))
