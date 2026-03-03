# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongclust(RPackage):
	"""Model-Based Clustering and Classification for Longitudinal Data

	Clustering or classification of longitudinal data based on a mixture of multivariate t or Gaussian distributions with a Cholesky-decomposed covariance structure. Details in McNicholas and Murphy (2010) <doi:10.1002/cjs.10047> and McNicholas and Subedi (2012) <doi:10.1016/j.jspi.2011.11.026>.
	"""
	
	cran = "longclust" 

	version("1.5", md5="c8960cb6c784d815bc40f1aa0a18938f")

	depends_on("r@4.3:", type=("build", "run"))
