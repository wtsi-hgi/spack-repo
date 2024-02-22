# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSihr(RPackage):
	"""Statistical Inference in High Dimensional Regression

	The goal of SIHR is to provide inference procedures in the high-dimensional setting for 
    (1) linear functionals in generalized linear regression ('Cai et al.' (2019) <arXiv:1904.12891>, 'Guo et al.' (2020) <arXiv:2012.07133>, 'Cai et al.' (2021)),
    (2) conditional average treatment effects in generalized linear regression,
    (3) quadratic functionals in generalized linear regression ('Guo et al.' (2019) <arXiv:1909.01503>).
    (4) inner product in generalized linear regression
    (5) distance in generalized linear regression.
	"""
	
	homepage = "https://github.com/prabrishar1/SIHR"
	cran = "SIHR" 

	version("2.0.1", md5="4f0becb5fb29e8fb1ef4d1771e64d7cc")

	depends_on("r-cvxr", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
