# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigora(RPackage):
	"""Signature Overrepresentation Analysis

	
     Pathway Analysis is statistically linking observations on 
     the molecular level to biological processes or pathways on 
     the systems(i.e., organism, organ, tissue, cell) level.  
     Traditionally, pathway analysis methods regard pathways 
     as collections of single genes and treat all genes in a pathway
     as equally informative. However, this can lead to identifying
     spurious pathways as statistically significant since components
     are often shared amongst pathways. SIGORA seeks to avoid this
     pitfall by focusing on genes or gene pairs that are (as a combination)
     specific to a single pathway.
     In relying on such pathway gene-pair signatures (Pathway-GPS),
     SIGORA inherently uses the status of other genes in the
     experimental context to identify the most relevant pathways.
     The current version allows for pathway analysis of human
     and mouse datasets. In addition, it contains pre-computed
     Pathway-GPS data for pathways in the KEGG and  Reactome
     pathway repositories and mechanisms for extracting GPS
     for user-supplied repositories.
	"""
	
	homepage = "https://github.com/wolski/sigora"
	cran = "sigora" 

	version("3.1.1", md5="24ab40ee407d180e54ba318a1de55d12")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
