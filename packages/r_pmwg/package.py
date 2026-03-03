# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmwg(RPackage):
	"""Particle Metropolis Within Gibbs

	Provides an R implementation of the Particle Metropolis within
    Gibbs sampler for model parameter, covariance matrix and random effect
    estimation. A more general implementation of the sampler based on the paper
    by Gunawan, D., Hawkins, G. E., Tran, M. N., Kohn, R., & Brown, S. D.
    (2020) <doi:10.1016/j.jmp.2020.102368>. An HTML tutorial document describing
    the package is available at
    <https://university-of-newcastle-research.github.io/samplerDoc/> and
    includes several detailed examples, some background and troubleshooting
    steps.
	"""
	
	homepage = "https://github.com/university-of-newcastle-research/pmwg"
	cran = "pmwg" 

	version("0.2.7", md5="c787b0ab49acc890e6a9f270a5e7eb74")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-condmvnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
