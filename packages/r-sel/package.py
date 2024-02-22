# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSel(RPackage):
	"""Semiparametric Elicitation

	Implements a method for fitting a bounded probability
        distribution to quantiles (for example stated by an expert),
        see Bornkamp and Ickstadt (2009) for details.  For this
        purpose B-splines are used, and the density is obtained by
        penalized least squares based on a Brier entropy penalty.  The
        package provides methods for fitting the distribution as well
        as methods for evaluating the underlying density and cdf. In
        addition methods for plotting the distribution, drawing random
        numbers and calculating quantiles of the obtained distribution
        are provided.
	"""
	
	cran = "SEL" 

	version("1.0-4", md5="92eee57722715b8bb8e81f68a2c60636")

	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
