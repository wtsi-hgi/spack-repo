# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvawkmt2(RPackage):
	"""Two-Sample Tests Based on Differences of Kaplan-Meier Curves

	Tests for equality of two survival functions based on integrated weighted differences of two Kaplan-Meier curves.
	"""
	
	cran = "survAWKMT2" 

	version("1.0.1", md5="a650b716ce0c75e099da35f1717f650d", url="https://cran.r-project.org/src/contrib/survAWKMT2_1.0.1.tar.gz")

	depends_on("r-survival", type=("build", "run"))
