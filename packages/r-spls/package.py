# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpls(RPackage):
	"""Sparse Partial Least Squares (SPLS) Regression and
Classification

	Provides functions for fitting a sparse
        partial least squares (SPLS) regression and classification
        (Chun and Keles (2010) <doi:10.1111/j.1467-9868.2009.00723.x>).
	"""
	
	cran = "spls" 

	version("2.2-3", md5="273e6be29dd0827df24d61180d78c74b")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
