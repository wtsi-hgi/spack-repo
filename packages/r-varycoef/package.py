# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarycoef(RPackage):
	"""Modeling Spatially Varying Coefficients

	Implements a maximum likelihood estimation (MLE) method for
    estimation and prediction of Gaussian process-based spatially varying
    coefficient (SVC) models (Dambon et al. (2021a)
    <doi:10.1016/j.spasta.2020.100470>).  Covariance tapering (Furrer et
    al. (2006) <doi:10.1198/106186006X132178>) can be applied such that
    the method scales to large data. Further, it implements a joint
    variable selection of the fixed and random effects (Dambon et al.
    (2021b) <doi:10.1080/13658816.2022.2097684>). The package and its 
    capabilities are described in (Dambon et al. (2021c) <arXiv:2106.02364>).
	"""
	
	homepage = "https://github.com/jakobdambon/varycoef"
	cran = "varycoef" 

	version("0.3.4", md5="4e5abde9f9da2191d5680a1f10257745")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-mlr", type=("build", "run"))
	depends_on("r-mlrmbo", type=("build", "run"))
	depends_on("r-optimparallel@0.8.1:", type=("build", "run"))
	depends_on("r-paramhelpers", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-smoof", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
