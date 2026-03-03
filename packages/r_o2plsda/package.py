# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RO2plsda(RPackage):
	"""Multiomics Data Integration

	Provides functions to do 'O2PLS-DA' analysis for multiple omics data integration.
            The algorithm came from "O2-PLS, a two-block (X±Y) latent variable regression (LVR) method with an integral OSC filter" 
            which published by Johan Trygg and Svante Wold at 2003 <doi:10.1002/cem.775>. 
            'O2PLS' is a bidirectional multivariate regression method that aims to separate the covariance between
            two data sets (it was recently extended to multiple data sets) (Löfstedt and Trygg, 2011 <doi:10.1002/cem.1388>; Löfstedt et al., 2012 <doi:10.1016/j.aca.2013.06.026>) 
            from the systematic sources of variance being specific for each data set separately. 
	"""
	
	cran = "o2plsda" 

	version("0.0.18", md5="4e39a766b4b3c9b0176b3e3a72130f6a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
