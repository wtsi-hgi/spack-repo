# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworkinference(RPackage):
	"""Inferring Latent Diffusion Networks

	This is an R implementation of the netinf algorithm (Gomez Rodriguez, Leskovec, and Krause, 2010)<doi:10.1145/1835804.1835933>. Given a set of events that spread between a set of nodes the algorithm infers the most likely stable diffusion network that is underlying the diffusion process.
	"""
	
	cran = "NetworkInference" 

	version("1.2.4", md5="a8fac12315abb0d139a4fad16534e0d5")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
