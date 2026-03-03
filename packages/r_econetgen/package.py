# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REconetgen(RPackage):
	"""Simulate and Sample from Ecological Interaction Networks

	Randomly generate a wide range of interaction networks with
             specified size, average degree, modularity, and topological
             structure. Sample nodes and links from within simulated networks
             randomly, by degree, by module, or by abundance. Simulations
             and sampling routines are implemented in 'FORTRAN', providing
             efficient generation times even for large networks. Basic
             visualization methods also included. Algorithms implemented
             here are described in de Aguiar et al. (2017) <arXiv:1708.01242>.
	"""
	
	homepage = "https://github.com/cboettig/EcoNetGen"
	cran = "EcoNetGen" 

	version("0.2.4", md5="c0e1b3aa22ab447d715e627d45d248b4")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
