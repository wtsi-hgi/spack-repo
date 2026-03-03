# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterplot(RPackage):
	"""Plot the Effects of Variables in Interaction Terms

	Plots the conditional coefficients ("marginal effects") of
    variables included in multiplicative interaction terms.
	"""
	
	cran = "interplot" 

	version("0.2.3", md5="b1c29f35d804e641c46a30d7f20576e3")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-interactiontest", type=("build", "run"))
