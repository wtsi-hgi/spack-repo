# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWhitestrap(RPackage):
	"""White Test and Bootstrapped White Test for Heteroskedasticity

	Formal implementation of White test of heteroskedasticity and a bootstrapped version of it, developed under the methodology of Jeong, J., Lee, K. (1999) <https://yonsei.pure.elsevier.com/en/publications/bootstrapped-whites-test-for-heteroskedasticity-in-regression-mod>.
	"""
	
	cran = "whitestrap" 

	version("0.0.1", md5="ee124b44d2595354ea24cf3aaaaa5119")

	depends_on("r@2.10:", type=("build", "run"))
