# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimest(RPackage):
	"""Constrained Single Index Model Estimation

	Estimation of function and index vector in single index model with and without shape constraints including different smoothness conditions.
	"""
	
	cran = "simest" 

	version("0.4", md5="5520a40cff2abcff7a334ef2eb8ef130")

	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-cobs", type=("build", "run"))
