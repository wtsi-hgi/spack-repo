# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvivalmodels(RPackage):
	"""Models for Survival Analysis

	Implementations of classical and machine learning models for survival analysis, including deep neural networks via 'keras' and 'tensorflow'. Each model includes a separated fit and predict interface with consistent prediction types for predicting risk or survival probabilities. Models are either implemented from 'Python' via 'reticulate' <https://CRAN.R-project.org/package=reticulate>, from code in GitHub packages, or novel implementations using 'Rcpp' <https://CRAN.R-project.org/package=Rcpp>. Neural networks are implemented from the 'Python' package 'pycox' <https://github.com/havakv/pycox>.
	"""
	
	homepage = "https://github.com/RaphaelS1/survivalmodels/"
	cran = "survivalmodels" 

	version("0.1.191", md5="ef07f43949486e09ef98bbfaa88379aa")
	version("0.1.13", md5="b4b410049e9b4d59c2e4f8f327559249")

	depends_on("r-rcpp", type=("build", "run"))
