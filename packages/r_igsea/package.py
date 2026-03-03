# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgsea(RPackage):
	"""Integrative Gene Set Enrichment Analysis Approaches

	To integrate multiple GSEA studies, we propose a hybrid strategy,
    iGSEA-AT, for choosing random effects (RE) versus fixed effect (FE) models,
    with an attempt to achieve the potential maximum statistical efficiency as 
    well as stability in performance in various practical situations. In addition
    to iGSEA-AT, this package also provides options to perform integrative GSEA
    with testing based on a FE model (iGSEA-FE) and testing based on a RE model
    (iGSEA-RE). The approaches account for different set sizes when testing a
    database of gene sets. The function is easy to use, and the three approaches
    can be applied to both binary and continuous phenotypes. 
	"""
	
	cran = "iGSEA" 

	version("1.2", md5="3056b3a574d6eb5717d4313926eb6932")

