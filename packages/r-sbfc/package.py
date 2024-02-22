# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbfc(RPackage):
	"""Selective Bayesian Forest Classifier

	An MCMC algorithm for simultaneous feature selection and classification, 
    and visualization of the selected features and feature interactions. 
    An implementation of SBFC by Krakovna, Du and Liu (2015), <arXiv:1506.02371>.
	"""
	
	homepage = "https://github.com/vkrakovna/sbfc"
	cran = "sbfc" 

	version("1.0.3", md5="fa67407f3651c1dbf8b6100761fba330")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-discretization", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
