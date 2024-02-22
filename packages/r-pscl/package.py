# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPscl(RPackage):
	"""Political Science Computational Laboratory

	Bayesian analysis of item-response theory (IRT) models,
  roll call analysis; computing highest density regions; 
  maximum likelihood estimation of zero-inflated and hurdle models for count data;
  goodness-of-fit measures for GLMs;
  data sets used in writing	and teaching; seats-votes curves.
	"""
	
	homepage = "https://github.com/atahk/pscl"
	cran = "pscl" 

	version("1.5.9", md5="c1a5bf7879e59bdc0889ee599e6c1375")

	depends_on("r-mass", type=("build", "run"))
