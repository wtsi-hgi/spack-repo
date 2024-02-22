# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMas(RPackage):
	"""Membership Association Studies

	Genome-wide association analysis that accommodate membership information, variance adjustment, and correlated responses.
	"""
	
	cran = "mas" 

	version("0.2.1", md5="0399c3c0557d15c94e976a4a4e194600")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-truncdist", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
