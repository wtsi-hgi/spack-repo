# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPgkdesphere(RPackage):
	"""Parametrically Guided Kernel Density Estimator for Spherical
Data

	Nonparametric density estimation for (hyper)spherical data by means of a parametrically guided kernel estimator (adaptation of the method of Hjort and Glad (1995) <doi:10.1214/aos/1176324627> to the spherical setting). The package also allows the data-driven selection of the smoothing parameter and the representation of the estimated density for circular and spherical data. Estimators of the density without guide can also be obtained.
	"""
	
	cran = "pgKDEsphere" 

	version("1.0.1", md5="75d799b6f1373a77743c66ae09384a93")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-directional", type=("build", "run"))
	depends_on("r-dirstats", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rotasym", type=("build", "run"))
	depends_on("r-movmf", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
