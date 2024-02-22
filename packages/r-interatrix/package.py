# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInteratrix(RPackage):
	"""Compute Chi-Square Measures with Corrections

	Chi-square tests are computed with corrections.
	"""
	
	homepage = "https://github.com/lbbe-software/Interatrix"
	cran = "Interatrix" 

	version("1.1.4", md5="b4860e40c6cbb2235d096a9e26cd8ae2")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
