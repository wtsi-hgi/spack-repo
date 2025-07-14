# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpnet(RPackage):
	"""Linear Programming Model for Network Inference

	lpNet aims at infering biological networks, in particular signaling and gene networks. For that it takes perturbation data, either steady-state or time-series, as input and generates an LP model which allows the inference of signaling networks. For parameter identification either leave-one-out cross-validation or stratified n-fold cross-validation can be used.
	"""
	
	bioc = "lpNet"

	version("2.40.0", commit="8efd48ecade3acb34e3c15c487297ecdc0e34694")
	version("2.34.2", commit="c28e516cf79aa2846fe11d2eebe72660197a6077")

	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-kegggraph", type=("build", "run"))
