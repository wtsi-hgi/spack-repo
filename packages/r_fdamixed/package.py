# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdamixed(RPackage):
	"""Functional Data Analysis in a Mixed Model Framework

	Likelihood based analysis of 1-dimension functional data
        in a mixed-effects model framework. Matrix computation are
        approximated by semi-explicit operator equivalents with linear
        computational complexity. Markussen (2013) <doi:10.3150/11-BEJ389>.
	"""
	
	cran = "fdaMixed" 

	version("0.6.1", md5="2eb95854eb8f86827c99007ac1f58e73")

	depends_on("r-formula", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
