# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPalm(RPackage):
	"""Fitting Point Process Models via the Palm Likelihood

	Functions to fit point process models using the Palm likelihood. First proposed by Tanaka, Ogata, and Stoyan (2008) <DOI:10.1002/bimj.200610339>, maximisation of the Palm likelihood can provide computationally efficient parameter estimation for point process models in situations where the full likelihood is intractable. This package is chiefly focused on Neyman-Scott point processes, but can also fit the void processes proposed by Jones-Todd et al. (2019) <DOI:10.1002/sim.8046>. The development of this package was motivated by the analysis of capture-recapture surveys on which individuals cannot be identified---the data from which can conceptually be seen as a clustered point process (Stevenson, Borchers, and Fewster, 2019 <DOI:10.1111/biom.12983>). As such, some of the functions in this package are specifically for the estimation of cetacean density from two-camera aerial surveys.
	"""
	
	homepage = "https://github.com/b-steve/palm"
	cran = "palm" 

	version("1.1.5", md5="6944eb7fed301192d018e8d2648afab0")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
