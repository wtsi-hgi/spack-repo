# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKcop(RPackage):
	"""Smooth Test for Equality of Copulas and Clustering Multivariate

	Implements approaches of non-parametric smooth test to 
            compare simultaneously K(K>1) copulas and non-parametric clustering 
            of multivariate populations with arbitrary sizes. 
            See Yves I. Ngounou Bakam and Denys Pommeret (2022) <arXiv:2112.05623> and
            Yves I. Ngounou Bakam and Denys Pommeret (2022) <arXiv:2211.06338>.
	"""
	
	cran = "Kcop" 

	version("1.0.0", md5="3e49b710cbdda799aeec5a4f41e16760")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
