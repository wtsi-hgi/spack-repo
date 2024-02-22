# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDnr(RPackage):
	"""Simulate Dynamic Networks using Exponential Random Graph Models
(ERGM) Family

	Functions are provided to fit temporal lag models to dynamic
    networks. The models are build on top of exponential random graph models (ERGM) framework. There are
    functions for simulating or forecasting networks for future time points.
    Abhirup Mallik & Zack W. Almquist (2019) Stable Multiple Time Step Simulation/Prediction From Lagged Dynamic Network Regression Models, Journal of Computational and Graphical Statistics, 28:4, 967-979, <DOI: 10.1080/10618600.2019.1594834>.
	"""
	
	cran = "dnr" 

	version("0.3.5", md5="4798bbf38545057f685ed3c02dc37bad")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
