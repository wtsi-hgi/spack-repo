# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPriogene(RPackage):
	"""Candidate Gene Prioritization for Non-Communicable Diseases
Based on Functional Information

	In gene sequencing methods, the topological features of protein-protein interaction (PPI) networks are 
    often used, such as ToppNet <https://toppgene.cchmc.org>. In this study, a candidate gene prioritization method
    was proposed for non-communicable diseases considering disease risks transferred between genes in weighted disease 
    PPI networks with weights for nodes and edges based on functional information.
	"""
	
	cran = "prioGene" 

	version("1.0.1", md5="68d44ce6dcf201a93077ff35534cc3cb")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
