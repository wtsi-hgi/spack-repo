# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlm(RPackage):
	"""Linear Models for Panel Data

	A set of estimators for models and (robust) covariance matrices, and tests for panel data
             econometrics, including within/fixed effects, random effects, between, first-difference, 
             nested random effects as well as instrumental-variable (IV) and Hausman-Taylor-style models,
             panel generalized method of moments (GMM) and general FGLS models,
             mean groups (MG), demeaned MG, and common correlated effects (CCEMG) and pooled (CCEP) estimators
             with common factors, variable coefficients and limited dependent variables models.
             Test functions include model specification, serial correlation, cross-sectional dependence,
             panel unit root and panel Granger (non-)causality. Typical references are general econometrics 
             text books such as Baltagi (2021), Econometric Analysis of Panel Data (<doi:10.1007/978-3-030-53953-5>),
             Hsiao (2014), Analysis of Panel Data (<doi:10.1017/CBO9781139839327>), and Croissant and Millo (2018), 
             Panel Data Econometrics with R (<doi:10.1002/9781119504641>).
	"""
	
	homepage = "https://cran.r-project.org/package=plm"
	cran = "plm" 

	version("2.6-4", md5="57da9057cb351e98cf3351074202af25")
	version("2.6-3", md5="d79cf0f7deb647e93921ebc699a26b4d")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-bdsmatrix", type=("build", "run"))
	depends_on("r-collapse@1.8.9:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
