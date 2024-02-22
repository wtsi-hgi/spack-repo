# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbcoptim(RPackage):
	"""Implementation of Artificial Bee Colony (ABC) Optimization

	An implementation of Karaboga (2005) Artificial Bee Colony
    Optimization algorithm <http://mf.erciyes.edu.tr/abc/pub/tr06_2005.pdf>.
    This (working) version is a Work-in-progress, which is
    why it has been implemented using pure R code. This was developed upon the basic
    version programmed in C and distributed at the algorithm's official website.
	"""
	
	homepage = "http://github.com/gvegayon/ABCoptim"
	cran = "ABCoptim" 

	version("0.15.0", md5="a62ed03650273c09899655065437078f")

	depends_on("r-rcpp", type=("build", "run"))
