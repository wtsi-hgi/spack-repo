# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCv(RPackage):
	"""Cross-Validation of Regression Models

	Cross-validation methods of regression models that exploit features of various
    modeling functions to improve speed. Some of the methods implemented in the package are
    novel, as described in the package vignettes; for general introductions to cross-validation,
    see, for example, Gareth James, Daniela Witten, Trevor Hastie, and Robert Tibshirani 
    (2021, ISBN 978-1-0716-1417-4, Secs. 5.1, 5.3), "An Introduction to Statistical Learning with 
    Applications in R, Second Edition", and Trevor Hastie, Robert Tibshirani, 
    and Jerome Friedman (2009, ISBN 978-0-387-84857-0, Sec. 7.10), "The Elements of Statistical 
    Learning, Second Edition".
	"""
	
	homepage = "https://gmonette.github.io/cv/"
	cran = "cv" 

	version("1.1.0", md5="3c6daf7294bd53a3169285a8ef253d1e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-insight", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
