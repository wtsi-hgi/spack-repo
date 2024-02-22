# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLqmm(RPackage):
	"""Linear Quantile Mixed Models

	Functions to fit quantile regression models for hierarchical
    data (2-level nested designs) as described in Geraci and
    Bottai (2014, Statistics and Computing) <doi:10.1007/s11222-013-9381-9>.
    A vignette is given in Geraci (2014, Journal of Statistical Software)
    <doi:10.18637/jss.v057.i13> and included in the package documents.
    The packages also provides functions to fit quantile models for
    independent	data and for count responses.
	"""
	
	cran = "lqmm" 

	version("1.5.8", md5="dcb1fa68aaf03e38b3cfcd2e78db03da")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-nlme@3.1.124:", type=("build", "run"))
	depends_on("r-sparsegrid", type=("build", "run"))
