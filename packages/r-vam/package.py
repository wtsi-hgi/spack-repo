# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVam(RPackage):
	"""Variance-Adjusted Mahalanobis

	Contains logic for cell-specific gene set scoring of single cell RNA sequencing data.
	"""
	
	cran = "VAM" 

	version("1.1.0", md5="2583e8a4fe9ceedc14cb233e3a7b16b5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
