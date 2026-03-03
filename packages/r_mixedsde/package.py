# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixedsde(RPackage):
	"""Estimation Methods for Stochastic Differential Mixed Effects
Models

	Inference on stochastic differential models Ornstein-Uhlenbeck or
    Cox-Ingersoll-Ross, with one or two random effects in the drift function.
	"""
	
	homepage = "https://cran.r-project.org/package=mixedsde"
	cran = "mixedsde" 

	version("5.0", md5="f1dfcf5c07df42e3ce92f101cb801e5e")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-sde", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
