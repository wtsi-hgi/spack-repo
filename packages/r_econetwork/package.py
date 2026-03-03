# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REconetwork(RPackage):
	"""Analyzing Ecological Networks

	A collection of advanced tools, methods and models specifically  designed  for  analyzing different  types  of  ecological  networks - especially  antagonistic  (food  webs,  host-parasite),  mutualistic (plant-pollinator, plant-fungus, etc)  and competitive networks, as well as their variability in time and space. Statistical models are developed to describe and understand the mechanisms that determine species interactions, and to decipher the organization of these ecological networks (Ohlmann et al. (2019)  <doi:10.1111/ele.13221>, Gonzalez et al. (2020) <doi:10.1101/2020.04.02.021691>, Miele et al. (2021) <doi:10.48550/arXiv.2103.10433>, Botella et al (2021) <doi:10.1111/2041-210X.13738>).
	"""
	
	homepage = "https://plmlab.math.cnrs.fr/econetproject/econetwork"
	cran = "econetwork" 

	version("0.7.0", md5="1e7f661dd13b920b896bf4da7fa9ffca")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rdiversity", type=("build", "run"))
	depends_on("r-blockmodels", type=("build", "run"))
	depends_on("r-bipartite", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
