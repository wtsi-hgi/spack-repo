# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrr(RPackage):
	"""Dimensionality Reduction via Regression

	An Implementation of Dimensionality Reduction
    via Regression using Kernel Ridge Regression.
	"""
	
	homepage = "https://github.com/gdkrmr/DRR"
	cran = "DRR" 

	version("0.0.4", md5="54da2f97bd8b0dd57137f98523c3fa0a")

	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-cvst", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
