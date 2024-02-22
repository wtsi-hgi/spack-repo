# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClhs(RPackage):
	"""Conditioned Latin Hypercube Sampling

	Conditioned Latin hypercube sampling, as published by Minasny and McBratney (2006) <DOI:10.1016/j.cageo.2005.12.009>. This method proposes to stratify sampling in presence of ancillary data. An extension of this method, which propose to associate a cost to each individual and take it into account during the optimisation process, is also proposed (Roudier et al., 2012, <DOI:10.1201/b12728>).
	"""
	
	homepage = "https://github.com/pierreroudier/clhs/"
	cran = "clhs" 

	version("0.9.0", md5="fa4e11287a46e91d66a53c2e93f69fd2")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
