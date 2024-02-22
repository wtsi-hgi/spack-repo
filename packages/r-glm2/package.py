# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlm2(RPackage):
	"""Fitting Generalized Linear Models

	Fits generalized linear models using the same model specification as glm in the stats package, but with a modified default fitting method that provides greater stability for models that may fail to converge using glm.
	"""
	
	cran = "glm2" 

	version("1.2.1", md5="fe8d4a7709bc259599bd61dd5442c492", url="https://cran.r-project.org/src/contrib/glm2_1.2.1.tar.gz")

	depends_on("r@3.2:", type=("build", "run"))
