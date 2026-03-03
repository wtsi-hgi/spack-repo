# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrenits(RPackage):
	"""Gene Regulatory Network Inference Using Time Series

	The package offers four network inference statistical models using Dynamic Bayesian Networks and Gibbs Variable Selection: a linear interaction model, two linear interaction models with added experimental noise (Gaussian and Student distributed) for the case where replicates are available and a non-linear interaction model.
	"""
	
	bioc = "GRENITS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GRENITS_1.54.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GRENITS/GRENITS_1.54.0.tar.gz"]

	version("1.54.0", md5="fd00e191f8c57c6ef54146263d21a089")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-ggplot2@0.9:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
