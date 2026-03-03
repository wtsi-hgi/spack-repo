# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REddington(RPackage):
	"""Compute a Cyclist's Eddington Number

	Compute a cyclist's Eddington number, including efficiently
    computing cumulative E over a vector. A cyclist's Eddington number
    <https://en.wikipedia.org/wiki/Arthur_Eddington#Eddington_number_for_cycling>
    is the maximum number satisfying the condition such that a cyclist has
    ridden E miles or greater on E distinct days. The algorithm in this package
    is an improvement over the conventional approach because both summary
    statistics and cumulative statistics can be computed in linear time, since
    it does not require initial sorting of the data. These functions may also be
    used for computing h-indices for authors, a metric described by Hirsch (2005)
    <doi:10.1073/pnas.0507655102>. Both are specific applications of computing
    the side length of a Durfee square <https://en.wikipedia.org/wiki/Durfee_square>.
	"""
	
	homepage = "https://github.com/pegeler/eddington2"
	cran = "eddington" 

	version("4.1.3", md5="8aad622ad64f170c53f966ad3321700e")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
