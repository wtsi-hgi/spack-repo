# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotmm(RPackage):
	"""Tidy Tools for Visualizing Mixture Models

	The main function, plot_mm(), is used for (gg)plotting output from mixture models, 
    including both densities and overlaying mixture weight component curves from the fit models in line with the
    tidy principles. The package includes several additional functions for added plot customization. 
    Supported model objects include: 'mixtools', 'EMCluster', and 'flexmix', with more from each in active dev. 
    Supported mixture model specifications include mixtures of univariate Gaussians, multivariate Gaussians, Gammas, 
    logistic regressions, linear regressions, and Poisson regressions.
	"""
	
	cran = "plotmm" 

	version("0.1.1", md5="1d5c06ff5e989833af623ff3e1fc6ccf")

	depends_on("r-wesanderson", type=("build", "run"))
	depends_on("r-amerika", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
