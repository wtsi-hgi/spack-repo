# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaleots(RPackage):
	"""Analyze Paleontological Time-Series

	Facilitates analysis of paleontological sequences of trait values.  
    Functions are provided to fit, using maximum likelihood, simple 
    evolutionary models (including unbiased random walks, directional 
    evolution,stasis, Ornstein-Uhlenbeck, covariate-tracking) and 
    complex models (punctuation, mode shifts).
	"""
	
	cran = "paleoTS" 

	version("0.5.3", md5="df711e738bfad5e1d289621d9461f418")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
