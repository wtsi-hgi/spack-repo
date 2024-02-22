# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRestriktor(RPackage):
	"""Restricted Statistical Estimation and Inference for Linear
Models

	Allow for easy-to-use testing or evaluating of linear equality and inequality restrictions about parameters and effects in (generalized) linear statistical models.
	"""
	
	homepage = "https://restriktor.org"
	cran = "restriktor" 

	version("0.5-30", md5="ec3023fa71654bd421e7c1f82c1be9fc")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-ic-infer", type=("build", "run"))
	depends_on("r-lavaan@0.6.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-norm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
