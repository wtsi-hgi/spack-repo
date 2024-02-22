# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsremlplus(RPackage):
	"""Augments 'ASReml-R' in Fitting Mixed Models and Packages
Generally in Exploring Prediction Differences

	Assists in automating the selection of terms to include in mixed models when  
  'asreml' is used to fit the models. Procedures are available for choosing models that 
  conform to the hierarchy or marginality principle, for fitting and choosing between 
  two-dimensional spatial models using correlation, natural cubic smoothing spline and 
  P-spline models. A history of the fitting of a sequence of models is kept in a data frame. 
  Also used to compute functions and contrasts of, to investigate differences between and 
  to plot predictions obtained using any model fitting function. The content  falls into 
  the following natural groupings: (i) Data, (ii) Model modification functions, (iii) Model 
  selection and description functions, (iv) Model diagnostics and simulation functions, 
  (v) Prediction production and presentation functions, (vi) Response transformation 
  functions, (vii) Object manipulation functions, and (viii) Miscellaneous functions 
  (for further details see 'asremlPlus-package' in help). The 'asreml' package provides a 
  computationally efficient algorithm for fitting a wide range of linear mixed models using 
  Residual Maximum Likelihood. It is a commercial package and a license for it can be 
  purchased from 'VSNi' <https://vsni.co.uk/> as 'asreml-R', who will supply a zip file 
  for local installation/updating (see <https://asreml.kb.vsni.co.uk/>). It is not needed 
  for functions that are methods for 'alldiffs'  and 'data.frame' objects. The package 
  'asremPlus' can also be installed from <http://chris.brien.name/rpackages/>.
	"""
	
	homepage = "http://chris.brien.name"
	cran = "asremlPlus" 

	version("4.4.27", md5="9971dd046956baaf72cc9645513007e0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dae", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-qqplotr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sticky", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
