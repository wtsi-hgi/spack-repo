# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMispu(RPackage):
	"""Microbiome Based Sum of Powered Score (MiSPU) Tests

	There is an increasing interest in investigating how the compositions of microbial communities are associated with human health and disease. In this package, we present a novel global testing method called aMiSPU, that is highly adaptive and thus high powered across various scenarios, alleviating the issue with the choice of a phylogenetic distance. Our simulations and real data analysis demonstrated that aMiSPU test was often more powerful than several competing methods while correctly controlling type I error rates.
	"""
	
	cran = "MiSPU" 

	version("1.0", md5="ead2aac012e15f1e85171f3d46553782")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-aspu", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
