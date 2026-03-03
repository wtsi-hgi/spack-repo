# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvlm(RPackage):
	"""Multivariate Linear Model with Analytic p-Values

	Allows a user to conduct multivariate multiple regression using analytic p-values rather than classic approximate F-tests.
	"""
	
	homepage = "http://github.com/dmcartor/MVLM"
	cran = "MVLM" 

	version("0.1.4", md5="1b9f1f922810b3868f0fc9a114833df0")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
