# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDart(RPackage):
	"""Denoising Algorithm based on Relevance network Topology

	Denoising Algorithm based on Relevance network Topology (DART) is an algorithm designed to evaluate the consistency of prior information molecular signatures (e.g in-vitro perturbation expression signatures) in independent molecular data (e.g gene expression data sets). If consistent, a pruning network strategy is then used to infer the activation status of the molecular signature in individual samples.
	"""
	
	bioc = "DART" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DART_1.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DART/DART_1.50.0.tar.gz"]

	version("1.50.0", md5="cc7bd6015b08890ec53f8004091c3bb5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph@0.6:", type=("build", "run"))
