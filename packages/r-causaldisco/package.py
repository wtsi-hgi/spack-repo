# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausaldisco(RPackage):
	"""Tools for Causal Discovery on Observational Data

	Various tools for inferring causal models from observational data. The package 
    includes an implementation of the temporal Peter-Clark (TPC) algorithm. Petersen, Osler 
    and Ekstrøm (2021) <doi:10.1093/aje/kwab087>. It also includes general tools
    for evaluating differences in adjacency matrices, which can be used for evaluating
    performance of causal discovery procedures. 
	"""
	
	homepage = "https://github.com/annennenne/causalDisco"
	cran = "causalDisco" 

	version("0.9.1", md5="cee295cf528de2fa74f002582d382235")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pcalg", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
