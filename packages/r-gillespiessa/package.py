# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGillespiessa(RPackage):
	"""Gillespie's Stochastic Simulation Algorithm (SSA)

	Provides a simple to use, intuitive, and
  extensible interface to several stochastic simulation
  algorithms for generating simulated trajectories of finite
  population continuous-time model. Currently it implements
  Gillespie's exact stochastic simulation algorithm (Direct
  method) and several approximate methods (Explicit tau-leap,
  Binomial tau-leap, and Optimized tau-leap). The package also
  contains a library of template models that can be run as demo
  models and can easily be customized and extended. Currently the
  following models are included, 'Decaying-Dimerization' reaction
  set, linear chain system, logistic growth model, 'Lotka'
  predator-prey model, Rosenzweig-MacArthur predator-prey model,
  'Kermack-McKendrick' SIR model, and a 'metapopulation' SIRS model.
  Pineda-Krch et al. (2008) <doi:10.18637/jss.v025.i12>.
	"""
	
	homepage = "https://github.com/rcannood/GillespieSSA"
	cran = "GillespieSSA" 

	version("0.6.2", md5="147b52b18bf984b603ff06942e8c06b9")

	depends_on("r@2:", type=("build", "run"))
