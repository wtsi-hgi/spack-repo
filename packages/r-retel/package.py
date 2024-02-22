# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRetel(RPackage):
	"""Regularized Exponentially Tilted Empirical Likelihood

	Implements the regularized exponentially tilted empirical 
    likelihood method. Details of the methods are given in Kim, MacEachern, and 
    Peruggia (2023) <doi:10.48550/arXiv.2312.17015>. This work was supported by 
    the U.S. National Science Foundation under Grants No. SES-1921523 and 
    DMS-2015552.
	"""
	
	homepage = "https://github.com/markean/retel"
	cran = "retel" 

	version("0.1.0", md5="b6ff5acc7161ab83737595e1954d0aba")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
