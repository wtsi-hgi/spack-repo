# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPresspurt(RPackage):
	"""Indeterminacy of Networks via Press Perturbations

	This is a computational package designed to identify the most sensitive interactions within a network which must be estimated most accurately in order to produce qualitatively robust predictions to a press perturbation. This is accomplished by enumerating the number of sign switches (and their magnitude) in the net effects matrix when an edge experiences uncertainty. The package produces data and visualizations when uncertainty is associated to one or more edges in the network and according to a variety of distributions. The software requires the network to be described by a system of differential equations but only requires as input a numerical Jacobian matrix evaluated at an equilibrium point. This package is based on Koslicki, D., & Novak, M. (2017) <doi:10.1007/s00285-017-1163-0>.
	"""
	
	homepage = "https://github.com/dkoslicki/PressPurt"
	cran = "PressPurt" 

	version("1.0.2", md5="35137b030504830a9ee32a98e95d50c3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-reticulate@1.11:", type=("build", "run"))
