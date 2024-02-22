# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTram(RPackage):
	"""Transformation Models

	Formula-based user-interfaces to specific transformation models
  implemented in package 'mlt'. Available models include Cox models, some parametric 
  survival models (Weibull, etc.), models for ordered categorical variables,
  normal and non-normal (Box-Cox type) linear models, and continuous outcome logistic regression
  (Lohse et al., 2017, <DOI:10.12688/f1000research.12934.1>). The underlying theory
  is described in Hothorn et al. (2018) <DOI:10.1111/sjos.12291>. An extension to
  transformation models for clustered data is provided (Barbanti and Hothorn, 2022,
  <DOI:10.1093/biostatistics/kxac048>). Multivariate conditional transformation models 
  (Klein et al, 2022, <DOI:10.1111/sjos.12501>) and shift-scale transformation models (Siegfried et al, 2023,
  <DOI:10.1080/00031305.2023.2203177>) can be fitted as well.
	"""
	
	homepage = "http://ctm.R-forge.R-project.org"
	cran = "tram" 

	version("1.0-2", md5="59f78d23b0fd52177386c2b318ad689e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mlt@1.5.0:", type=("build", "run"))
	depends_on("r-mvtnorm@1.2.0:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-variables@1.0.4:", type=("build", "run"))
	depends_on("r-basefun@1.1.2:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
