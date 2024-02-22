# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLikelihoodexplore(RPackage):
	"""Likelihood Exploration

	Provides likelihood functions as defined by Fisher (1922)
    <doi:10.1098/rsta.1922.0009> and a function that creates likelihood 
    functions from density functions. The functions are meant to aid in 
    education of likelihood based methods.
	"""
	
	homepage = "https://likelihoodExplore.bearstatistics.com"
	cran = "likelihoodExplore" 

	version("0.1.0", md5="5e303d4f87e91b6808cb3248e808b7ba")

	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
