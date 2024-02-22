# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXutils(RPackage):
	"""Utility Functions of Fangzhou Xie

	This is a collection of some useful functions when dealing with text data. 
    Currently it only contains a very efficient function of decoding HTML entities
    in character vectors by 'Rcpp' routine.
	"""
	
	homepage = "https://github.com/fangzhou-xie/xutils"
	cran = "xutils" 

	version("0.0.2", md5="e1d69cb96cb83797e99b86b79fb643e3")

	depends_on("r-rcpp", type=("build", "run"))
