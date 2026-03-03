# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbnpa(RPackage):
	"""Permutation Based Non-Parametric Analysis of CRISPR Screen Data

	Permutation based
    non-parametric analysis of CRISPR screen data. Details about this algorithm are published in the following paper published on BMC genomics, Jia et al. (2017) <doi:10.1186/s12864-017-3938-5>: A permutation-based non-parametric analysis of CRISPR screen data. Please cite this paper if you use this algorithm for your paper.
	"""
	
	cran = "PBNPA" 

	version("0.0.3", md5="aef459320112dd9103ddc4f3fa186f31")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-metarnaseq", type=("build", "run"))
