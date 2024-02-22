# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInvertiforms(RPackage):
	"""Invertible Transforms for Matrices

	Provides composable invertible transforms for
    (sparse) matrices.
	"""
	
	homepage = "https://rohelab.github.io/invertiforms/"
	cran = "invertiforms" 

	version("0.1.1", md5="55f37caa27cb0e2652615ad2702454f4")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sparselrmatrix@0.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
