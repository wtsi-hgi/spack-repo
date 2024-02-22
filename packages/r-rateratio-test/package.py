# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRateratioTest(RPackage):
	"""Exact Rate Ratio Test

	Performs exact rate ratio tests.
	"""
	
	cran = "rateratio.test" 

	version("1.1", md5="2f0eb8b9a020ad972b6f9fff13f528ce")

	depends_on("r@2.4.1:", type=("build", "run"))
