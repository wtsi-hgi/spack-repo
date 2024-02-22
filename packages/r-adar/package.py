# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdar(RPackage):
	"""A Fast 'WHATWG' Compliant URL Parser

	A wrapper for 'ada-url', a 'WHATWG' compliant and fast URL parser written in modern 'C++'. Also contains auxiliary functions such as a public suffix extractor.
	"""
	
	homepage = "https://gesistsa.github.io/adaR/"
	cran = "adaR" 

	version("0.3.2", md5="964a83cb37edfd76a8f0779fa7ab9686")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-triebeard", type=("build", "run"))
