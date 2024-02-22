# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetdiffuser(RPackage):
	"""Analysis of Diffusion and Contagion Processes on Networks

	Empirical statistical analysis, visualization and simulation of
    diffusion and contagion processes on networks. The package implements algorithms
    for calculating network diffusion statistics such as transmission rate, hazard
    rates, exposure models, network threshold levels, infectiousness (contagion),
    and susceptibility. The package is inspired by work published in Valente,
    et al., (2015) <DOI:10.1016/j.socscimed.2015.10.001>; Valente (1995) <ISBN:
    9781881303213>, Myers (2000) <DOI:10.1086/303110>, Iyengar and others (2011)
    <DOI:10.1287/mksc.1100.0566>, Burt (1987) <DOI:10.1086/228667>; among others.
	"""
	
	homepage = "https://github.com/USCCANA/netdiffuseR"
	cran = "netdiffuseR" 

	version("1.22.6", md5="b8a5d9148f81fff2683bd312e7a94fa4")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-networkdynamic", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matchit", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
