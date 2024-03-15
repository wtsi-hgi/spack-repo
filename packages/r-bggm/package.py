# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBggm(RPackage):
	"""Bayesian Gaussian Graphical Models

	Fit Bayesian Gaussian graphical models. The methods are separated into 
    two Bayesian approaches for inference: hypothesis testing and estimation. There are 
    extensions for confirmatory hypothesis testing, comparing Gaussian graphical models, 
    and node wise predictability. These methods were recently introduced in the Gaussian 
    graphical model literature, including 
    Williams (2019) <doi:10.31234/osf.io/x8dpr>, 
    Williams and Mulder (2019) <doi:10.31234/osf.io/ypxd8>,
    Williams, Rast, Pericchi, and Mulder (2019) <doi:10.31234/osf.io/yt386>.
	"""
	
	cran = "BGGM" 

	version("2.1.1", md5="6b019322c826b0be32034a946842bfc0")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-bfpack@1.2.3:", type=("build", "run"))
	depends_on("r-ggally@1.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-ggridges@0.5.1:", type=("build", "run"))
	depends_on("r-mass@7.3.51.5:", type=("build", "run"))
	depends_on("r-mvnfast@0.2.5:", type=("build", "run"))
	depends_on("r-network@1.15:", type=("build", "run"))
	depends_on("r-reshape@0.8.8:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack@0.11.1:", type=("build", "run"))
	depends_on("r-sna@2.5:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppdist", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
