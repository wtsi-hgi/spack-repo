# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThames(RPackage):
	"""Truncated Harmonic Mean Estimator of the Marginal Likelihood

	Implements the truncated harmonic mean estimator (THAMES) 
    of the reciprocal marginal likelihood using posterior samples and
    unnormalized log posterior values via reciprocal importance sampling.
    Metodiev, Perrot-Dockès, Ouadah, Irons, & Raftery (2023) <arXiv:2305.08952>.
	"""
	
	cran = "thames" 

	version("0.1.1", md5="caae19780d0dd03b82ea370af34a40e0")

	depends_on("r-uniformly", type=("build", "run"))
