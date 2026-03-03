# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpnngp(RPackage):
	"""Spatial Regression Models for Large Datasets using Nearest
Neighbor Gaussian Processes

	Fits univariate Bayesian spatial regression models for large datasets using Nearest Neighbor Gaussian Processes (NNGP) detailed in Finley, Datta, Banerjee (2022) <doi:10.18637/jss.v103.i05>, Finley, Datta, Cook, Morton, Andersen, and Banerjee (2019) <doi:10.1080/10618600.2018.1537924>, and Datta, Banerjee, Finley, and Gelfand (2016) <doi:10.1080/01621459.2015.1044091>.
	"""
	
	homepage = "https://www.finley-lab.com/"
	cran = "spNNGP" 

	version("1.0.0", md5="7adf211523652c49e3cffa1159ad5d68")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
