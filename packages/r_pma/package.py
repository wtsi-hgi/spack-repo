# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPma(RPackage):
	"""Penalized Multivariate Analysis

	Performs Penalized Multivariate Analysis: a penalized
        matrix decomposition, sparse principal components analysis,
        and sparse canonical correlation analysis, described in
        Witten, Tibshirani and Hastie (2009)
        <doi:10.1093/biostatistics/kxp008> and Witten and Tibshirani
        (2009) Extensions of sparse canonical correlation analysis,
        with applications to genomic data
        <doi:10.2202/1544-6115.1470>.
	"""
	
	homepage = "https://github.com/bnaras/PMA"
	cran = "PMA" 

	version("1.2-3", md5="f4761339585ee1f7a86562b6863cd985")

	depends_on("r@2.10:", type=("build", "run"))
