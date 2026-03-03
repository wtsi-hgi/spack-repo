# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransphylo(RPackage):
	"""Inference of Transmission Tree from a Dated Phylogeny

	Inference of transmission tree from a dated phylogeny. 
    Includes methods to simulate and analyse outbreaks.
    The methodology is described in
    Didelot et al. (2014) <doi:10.1093/molbev/msu121>,
    Didelot et al. (2017) <doi:10.1093/molbev/msw275>.
	"""
	
	cran = "TransPhylo" 

	version("1.4.5", md5="fd3b2ab8c187fe56003c5046cc71c2d2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
