# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotgmm(RPackage):
	"""Tools for Visualizing Gaussian Mixture Models

	The main function, plot_GMM, is used for plotting output from Gaussian mixture models (GMMs), 
    including both densities and overlaying mixture weight component curves from the fit GMM. The package
    also include the function, plot_cut_point, which plots the cutpoint (mu) from the GMM over a histogram
    of the distribution with several color options. Finally, the package includes the function, plot_mix_comps, 
    which is used in the plot_GMM function, and can be used to create a custom plot for overlaying mixture 
    component curves from GMMs. For the plot_mix_comps function, usage most often will be specifying 
    the "fun" argument within "stat_function" in a ggplot2 object.
	"""
	
	cran = "plotGMM" 

	version("0.2.2", md5="9d48bcfbba26fd776d5cb4754c322a7d")

	depends_on("r-wesanderson", type=("build", "run"))
	depends_on("r-amerika", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
