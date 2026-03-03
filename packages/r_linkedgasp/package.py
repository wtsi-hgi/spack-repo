# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinkedgasp(RPackage):
	"""Linked Emulator of a Coupled System of Simulators

	Prototypes for construction of a Gaussian Stochastic Process emulator (GASP) of a computer model. This is done within the objective Bayesian implementation of the GASP. The package allows for construction of a linked GASP of the composite computer model. Computational implementation follows the mathematical exposition given in publication: Ksenia N. Kyzyurova, James O. Berger, Robert L. Wolpert. Coupling computer models through linking their statistical emulators. SIAM/ASA Journal on Uncertainty Quantification, 6(3): 1151-1171, (2018).<DOI:10.1137/17M1157702>.
	"""
	
	cran = "LinkedGASP" 

	version("1.0", md5="27ed4c7ea7353a2cc66dadf154787aea")

	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-spbayes", type=("build", "run"))
