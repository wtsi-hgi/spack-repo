# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdglm(RPackage):
	"""Tests for High Dimensional Generalized Linear Models

	Test the significance of coefficients in high dimensional generalized linear models.
	"""
	
	cran = "HDGLM" 

	version("0.1", md5="d81e6c574e9a663d34d0983dc1a6c441")

	depends_on("r@3.1.1:", type=("build", "run"))
