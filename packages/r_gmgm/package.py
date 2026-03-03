# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmgm(RPackage):
	"""Gaussian Mixture Graphical Model Learning and Inference

	Gaussian mixture graphical models include Bayesian networks and
    dynamic Bayesian networks (their temporal extension) whose local probability
    distributions are described by Gaussian mixture models. They are powerful
    tools for graphically and quantitatively representing nonlinear dependencies
    between continuous variables. This package provides a complete framework to
    create, manipulate, learn the structure and the parameters, and perform
    inference in these models. Most of the algorithms are described in the PhD
    thesis of Roos (2018) <https://tel.archives-ouvertes.fr/tel-01943718>.
	"""
	
	cran = "gmgm" 

	version("1.1.2", md5="46c134409256a6ce91a97e614300a3e6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-visnetwork@2.0.8:", type=("build", "run"))
