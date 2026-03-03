# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcge(RPackage):
	"""Estimation of Number of Clusters and Identification of Atypical
Units

	It is a package that helps to estimate the number of real clusters in data as well as to identify atypical units. The underlying methods are based on distances rather than on unit x variables.
	"""
	
	cran = "ICGE" 

	version("0.4.2", md5="85afab96fa72d6ee928315c107310d12")

	depends_on("r@2.0.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
