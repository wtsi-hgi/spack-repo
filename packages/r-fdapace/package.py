# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdapace(RPackage):
	"""Functional Data Analysis and Empirical Dynamics

	A versatile package that provides implementation of various
    methods of Functional Data Analysis (FDA) and Empirical Dynamics. The core of this
    package is Functional Principal Component Analysis (FPCA), a key technique for
    functional data analysis, for sparsely or densely sampled random trajectories
    and time courses, via the Principal Analysis by Conditional Estimation
    (PACE) algorithm. This core algorithm yields covariance and mean functions,
    eigenfunctions and principal component (scores), for both functional data and
    derivatives, for both dense (functional) and sparse (longitudinal) sampling designs.
    For sparse designs, it provides fitted continuous trajectories with confidence bands,
    even for subjects with very few longitudinal observations. PACE is a viable and
    flexible alternative to random effects modeling of longitudinal data. There is also a
    Matlab version (PACE) that contains some methods not available on fdapace and vice
    versa. Updates to fdapace were supported by grants from NIH Echo and NSF DMS-1712864 and DMS-2014626. Please cite our package if you use it (You may run the command citation("fdapace") to get the citation format and bibtex entry).
    References: Wang, J.L., Chiou, J., Müller, H.G. (2016) <doi:10.1146/annurev-statistics-041715-033624>;
    Chen, K., Zhang, X., Petersen, A., Müller, H.G. (2017) <doi:10.1007/s12561-015-9137-5>.
	"""
	
	homepage = "https://github.com/functionaldata/tPACE"
	cran = "fdapace" 

	version("0.5.9", md5="91cd064c9ece0583db24d21355a5b329")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
