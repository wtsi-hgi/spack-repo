# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneralizedwendland(RPackage):
	"""Fully Parameterized Generalized Wendland Covariance Function

	A fully parameterized Generalized Wendland covariance function for use in Gaussian process models, as well as multiple methods for approximating it via covariance interpolation. The available methods are linear interpolation, polynomial interpolation, and cubic spline interpolation.
  Moreno Bevilacqua and Reinhard Furrer and Tarik Faouzi and Emilio Porcu (2019) <url:<https://projecteuclid.org/journalArticle/Download?urlId=10.1214%2F17-AOS1652 >>.
  Moreno Bevilacqua and Christian Caamaño-Carrillo and Emilio Porcu (2022) <arXiv:2008.02904>.
  Reinhard Furrer and Roman Flury and Florian Gerber (2022) <url:<https://CRAN.R-project.org/package=spam >>.
	"""
	
	cran = "GeneralizedWendland" 

	version("0.6.0", md5="e12693f619ccf4668c4d36c8ac06b5d2")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-spam64", type=("build", "run"))
	depends_on("r-optimparallel", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("gsl@2.7:", type=("build", "link", "run"))
