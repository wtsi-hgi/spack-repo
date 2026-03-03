# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtmpt(RPackage):
	"""Fitting (Exponential/Diffusion) RT-MPT Models

	Fit (exponential or diffusion) response-time extended multinomial processing tree (RT-MPT) models 
      by Klauer and	Kellen (2018) <doi:10.1016/j.jmp.2017.12.003> and Klauer, Hartmann, and Meyer-Grant (submitted). 
      The RT-MPT class not only incorporate	frequencies like traditional multinomial processing tree (MPT) models, 
      but also latencies. This enables it	to estimate process completion times and encoding plus motor execution times 
      next to the process probabilities	of traditional MPTs. 'rtmpt' is a hierarchical Bayesian framework and posterior 
      samples are sampled using a Metropolis-within-Gibbs sampler (for exponential RT-MPTs) or Hamiltonian-within-Gibbs 
      sampler (for diffusion RT-MPTs).
	"""
	
	cran = "rtmpt" 

	version("2.0-0", md5="688b85b48592862310bca61723a7d05b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-ryacas", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("gsl@2.3:", type=("build", "link", "run"))
