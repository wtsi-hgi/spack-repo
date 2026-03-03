# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTernarynet(RPackage):
	"""Ternary Network Estimation

	Gene-regulatory network (GRN) modeling seeks to infer dependencies between genes and thereby provide insight into the regulatory relationships that exist within a cell. This package provides a computational Bayesian approach to GRN estimation from perturbation experiments using a ternary network model, in which gene expression is discretized into one of 3 states: up, unchanged, or down). The ternarynet package includes a parallel implementation of the replica exchange Monte Carlo algorithm for fitting network models, using MPI.
	"""
	
	bioc = "ternarynet" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ternarynet_1.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ternarynet/ternarynet_1.46.0.tar.gz"]

	version("1.46.0", md5="1ee0ac867354eedf8cf756d94be52589")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
