# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWsprv(RPackage):
	"""Weighted Selection Probability for Rare Variant Analysis

	A weighted selection probability to locate rare variants associated with multiple phenotypes.
	"""
	
	cran = "wsprv" 

	version("0.1.0", md5="8de759699f93da1db1c7d18790ebc9ea")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
