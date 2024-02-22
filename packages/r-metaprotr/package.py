# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaprotr(RPackage):
	"""Metaproteomics Post-Processing Analysis

	
    Set of tools for descriptive analysis of metaproteomics data generated from high-throughput 
    mass spectrometry instruments. These tools allow to cluster peptides and proteins abundance, 
    expressed as spectral counts, and to manipulate them in groups of metaproteins. This information 
    can be represented using multiple visualization functions to portray the global metaproteome 
    landscape and to differentiate samples or conditions, in terms of abundance of metaproteins, 
    taxonomic levels and/or functional annotation. The provided tools allow to implement flexible 
    analytical pipelines that can be easily applied to studies interested in metaproteomics analysis.
	"""
	
	homepage = "https://forgemia.inra.fr/pappso/metaprotr"
	cran = "metaprotr" 

	version("1.2.2", md5="a82e43105f9d527eb44b4dd26f19ec45")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
