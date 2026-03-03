# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViking(RPackage):
	"""State-Space Models Inference by Kalman or Viking

	Inference methods for state-space models, relying on the Kalman Filter or on Viking (Variational Bayesian VarIance tracKING). See J. de Vilmarest (2022) <https://theses.hal.science/tel-03716104/>.
	"""
	
	cran = "viking" 

	version("1.0.2", md5="044c233005fb386c6c4451b0f54e5217")

