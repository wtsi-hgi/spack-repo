# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMegena(RPackage):
	"""Multiscale Clustering of Geometrical Network

	Co-Expression Network Analysis by adopting network embedding technique. Song W.-M., Zhang B. (2015) Multiscale Embedded Gene Co-expression Network Analysis. PLoS Comput Biol 11(11): e1004574. <doi: 10.1371/journal.pcbi.1004574>.
	"""
	
	homepage = "https://github.com/songw01/MEGENA"
	cran = "MEGENA" 

	version("1.3.7", md5="f35b33624e9a61d9eda5780c684202b2")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-doparallel@1.0.11:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
	depends_on("r-igraph@1.2.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix@1.1.5:", type=("build", "run"))
	depends_on("r-ggplot2@1:", type=("build", "run"))
	depends_on("r-reshape@0.8.5:", type=("build", "run"))
	depends_on("r-fpc@2.1.11:", type=("build", "run"))
	depends_on("r-cluster@2.0.7.1:", type=("build", "run"))
	depends_on("r-ggrepel@0.5:", type=("build", "run"))
	depends_on("r-ggraph@1.0.1:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
