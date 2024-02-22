# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamlss(RPackage):
	"""Generalised Additive Models for Location Scale and Shape.

	Functions for fitting the Generalized Additive Models for Location Scale
	and Shape introduced by Rigby and Stasinopoulos (2005),
	<doi:10.1111/j.1467-9876.2005.00510.x>. The models use a distributional
	regression approach where all the parameters of the conditional
	distribution of the response variable are modelled using explanatory
	variables."""

	cran = "gamlss"

	version("5.4-20", md5="f92b31f8e7440afabf4b1eb6316d021f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-gamlss-data@5.0.0:", type=("build", "run"))
	depends_on("r-gamlss-dist@4.3.1:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
