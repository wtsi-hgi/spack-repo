# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasybgm(RPackage):
	"""Extracting and Visualizing Bayesian Graphical Models

	Fit and visualize the results of a Bayesian analysis of networks commonly found in psychology. 
    The package supports fitting cross-sectional network models fitted using the packages 'BDgraph', 'bgms' and 'BGGM'. 
    The package provides the parameter estimates, posterior inclusion probabilities, inclusion Bayes factor, and the 
    posterior density of the parameters. In addition, for 'BDgraph' and 'bgms' it allows to assess the posterior 
    structure space. Furthermore, the package comes with an extensive suite for visualizing results.
	"""
	
	homepage = "https://github.com/KarolineHuth/easybgm"
	cran = "easybgm" 

	version("0.1.2", md5="c7f06fa29b9e9849b8ac581fa520ae26")

	depends_on("r-bdgraph", type=("build", "run"))
	depends_on("r-bggm", type=("build", "run"))
	depends_on("r-bgms@0.1.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hdinterval", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
