# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUncover(RPackage):
	"""Utilising Normalisation Constant Optimisation via Edge Removal
(UNCOVER)

	Model data with a suspected clustering structure (either in 
    co-variate space, regression space or both) using a Bayesian product model 
    with a logistic regression likelihood. Observations are represented 
    graphically and clusters are formed through various edge removals or 
    additions. Cluster quality is assessed through the log Bayesian evidence of 
    the overall model, which is estimated using either a Sequential Monte Carlo 
    sampler or a suitable transformation of the Bayesian Information Criterion 
    as a fast approximation of the former. The internal Iterated Batch 
    Importance Sampling scheme (Chopin (2002 <doi:10.1093/biomet/89.3.539>)) is 
    made available as a free standing function.
	"""
	
	cran = "UNCOVER" 

	version("1.1.0", md5="38dbc14f281d0dfe629ae6603b6f0061")

	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-cachem", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
