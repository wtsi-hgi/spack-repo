# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBicorn(RPackage):
	"""Integrative Inference of De Novo Cis-Regulatory Modules

	Prior transcription factor binding knowledge and target gene expression data are integrated in a Bayesian framework for functional cis-regulatory module inference. Using Gibbs sampling, we iteratively estimate transcription factor associations for each gene, regulation strength for each binding event and the hidden activity for each transcription factor.  
	"""
	
	cran = "BICORN" 

	version("0.1.0", md5="bf9ea3f43e5893aa6a30be34c546e8af")

	depends_on("r@3.4:", type=("build", "run"))
