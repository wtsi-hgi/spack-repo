# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrpack(RPackage):
	"""Reduced-Rank Regression

	Multivariate regression methodologies including
    classical reduced-rank regression (RRR)
    studied by Anderson (1951) <doi:10.1214/aoms/1177729580> and
    Reinsel and Velu (1998) <doi:10.1007/978-1-4757-2853-8>,
    reduced-rank regression via adaptive nuclear norm penalization
    proposed by Chen et al. (2013) <doi:10.1093/biomet/ast036> and
    Mukherjee et al. (2015) <doi:10.1093/biomet/asx080>,
    robust reduced-rank regression (R4) proposed by
    She and Chen (2017) <doi:10.1093/biomet/asx032>,
    generalized/mixed-response reduced-rank regression (mRRR) proposed by
    Luo et al. (2018) <doi:10.1016/j.jmva.2018.04.011>,
    row-sparse reduced-rank regression (SRRR) proposed by
    Chen and Huang (2012) <doi:10.1080/01621459.2012.734178>,
    reduced-rank regression with a sparse singular value decomposition (RSSVD)
    proposed by Chen et al. (2012) <doi:10.1111/j.1467-9868.2011.01002.x>
    and sparse and orthogonal factor regression (SOFAR) proposed by
    Uematsu et al. (2019) <doi:10.1109/TIT.2019.2909889>.
	"""
	
	cran = "rrpack" 

	version("0.1-13", md5="30d270dbb38ea6f5c645d4b26f8a29b6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
