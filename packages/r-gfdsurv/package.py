# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGfdsurv(RPackage):
	"""Tests for Survival Data in General Factorial Designs

	Implemented are three Wald-type statistic and respective
  permuted versions for null hypotheses formulated in terms of cumulative hazard rate functions, medians and the concordance measure, respectively, in the general framework of survival factorial designs with possibly heterogeneous survival and/or censoring distributions, for crossed designs with an arbitrary number of factors and nested designs with up to three factors.
	Ditzhaus, Dobler and Pauly (2020) <doi:10.1177/0962280220980784> 
	Ditzhaus, Janssen, Pauly (2020) <arXiv: 2004.10818v2>
	Dobler and Pauly (2019) <doi:10.1177/0962280219831316>.
	"""
	
	homepage = "https://github.com/PhilippSteinhauer/GFDsurv"
	cran = "GFDsurv" 

	version("0.1.1", md5="9561910b46b3b0cc23ee7d7ade4e507f")

	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-shinyjs@2:", type=("build", "run"))
	depends_on("r-shinythemes@1.1.2:", type=("build", "run"))
	depends_on("r-survival@3.2.7:", type=("build", "run"))
	depends_on("r-survminer@0.4.8:", type=("build", "run"))
	depends_on("r-tippy@0.1:", type=("build", "run"))
	depends_on("r-magic@1.5.9:", type=("build", "run"))
	depends_on("r-mass@7.3.53:", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
