# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsenet(RPackage):
	"""Fit Sparse Linear Regression Models via Nonconvex Optimization

	Efficient procedure for fitting regularization paths between L1 and L0, using the MC+ penalty of Zhang, C.H. (2010)<doi:10.1214/09-AOS729>. Implements the methodology described in Mazumder, Friedman and Hastie (2011) <DOI: 10.1198/jasa.2011.tm09738>. Sparsenet computes the regularization surface over both the family parameter and the tuning parameter by coordinate descent.
	"""
	
	homepage = "https://hastie.su.domains/public/Papers/Sparsenet/Mazumder-SparseNetCoordinateDescent-2011.pdf"
	cran = "sparsenet" 

	version("1.6", md5="d6fb54a2b8b7ddc33b2ec85d647654c9")

	depends_on("r-matrix@1.0.6:", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
