# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPseudorank(RPackage):
	"""Pseudo-Ranks

	Efficient calculation of pseudo-ranks and (pseudo)-rank based test statistics. In case of equal sample sizes, pseudo-ranks and mid-ranks are equal. When used for inference mid-ranks may lead to paradoxical results. Pseudo-ranks are in general not affected by such a problem <doi:10.18637/jss.v095.c01>.
	"""
	
	homepage = "https://github.com/happma/pseudorank/"
	cran = "pseudorank" 

	version("1.0.1", md5="50f47aecdca28edacd36c01d9e71f8af")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-doby", type=("build", "run"))
