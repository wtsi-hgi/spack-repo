# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmcensemble(RPackage):
	"""Ensemble Sampler for Affine-Invariant MCMC

	Provides ensemble samplers for
    affine-invariant Monte Carlo Markov Chain, which allow a faster
    convergence for badly scaled estimation problems. Two samplers are
    proposed: the 'differential.evolution' sampler from ter Braak and
    Vrugt (2008) <doi:10.1007/s11222-008-9104-9> and the 'stretch' sampler
    from Goodman and Weare (2010) <doi:10.2140/camcos.2010.5.65>.
	"""
	
	homepage = "https://github.com/Bisaloo/mcmcensemble"
	cran = "mcmcensemble" 

	version("3.0.0", md5="184a2eca814a4564c4fa688a098eb477")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
