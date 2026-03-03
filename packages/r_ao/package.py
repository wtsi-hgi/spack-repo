# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAo(RPackage):
	"""Alternating Optimization

	Alternating optimization of (high-dimensional) functions is an 
    iterative procedure for optimizing jointly over all parameters by 
    alternately optimizing parameter subsets.
	"""
	
	homepage = "https://loelschlaeger.de/ao/"
	cran = "ao" 

	version("0.3.3", md5="655e7ff1927686e89018e06349568a35")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-optimizer@1.0.4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-oeli", type=("build", "run"))
