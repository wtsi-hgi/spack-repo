# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdjm(RPackage):
	"""Penalized High-Dimensional Joint Model

	Joint models have been widely used to study the associations between longitudinal biomarkers and a survival outcome. However, existing joint models only consider one or a few longitudinal 
    biomarkers and cannot deal with high-dimensional longitudinal biomarkers. This package can be used to fit our recently developed penalized joint model that can handle high-dimensional longitudinal biomarkers. 
    Specifically, an adaptive lasso penalty is imposed on the parameters for the effects of the longitudinal biomarkers on the survival outcome, which allows for variable selection. 
    Also, our algorithm is computationally efficient, which is based on the Gaussian variational approximation method.
	"""
	
	cran = "HDJM" 

	version("0.1.0", md5="65b61c5e0f44c6918de3c7e023dcd9b8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survival@3.2:", type=("build", "run"))
	depends_on("r-statmod@1.4:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppensmallen", type=("build", "run"))
