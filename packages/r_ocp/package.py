# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROcp(RPackage):
	"""Bayesian Online Changepoint Detection

	Implements the Bayesian online changepoint
     detection method by Adams and MacKay (2007) 
     <arXiv:0710.3742> for univariate or multivariate data.
     Gaussian and Poisson probability models are implemented.
      Provides post-processing functions with 
      alternative ways to extract changepoints.
	"""
	
	cran = "ocp" 

	version("0.1.1", md5="8b5ff659839749886937bcb5e3c50b40")

	depends_on("r@3.4:", type=("build", "run"))
