# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactmle(RPackage):
	"""Maximum Likelihood Factor Analysis

	Perform Maximum Likelihood Factor analysis on a covariance matrix or data matrix.
	"""
	
	cran = "FACTMLE" 

	version("1.1", md5="548719ece73d1144bfe09c2e9f8fa981")

	depends_on("r-rarpack", type=("build", "run"))
