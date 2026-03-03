# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwid(RPackage):
	"""Genome-Wide Identity-by-Descent

	Methods and tools for the analysis of Genome Wide 
    Identity-by-Descent ('gwid') mapping data, focusing on testing whether there 
    is a higher occurrence of Identity-By-Descent (IBD) segments around potential causal variants 
    in cases compared to controls, which is crucial for identifying rare 
    variants. To enhance its analytical power, 'gwid' incorporates a Sliding 
    Window Approach, allowing for the detection and analysis of signals from 
    multiple Single Nucleotide Polymorphisms (SNPs).
	"""
	
	homepage = "https://github.com/soroushmdg/gwid"
	cran = "gwid" 

	version("0.1.0", md5="edb5dc1780eab50bf4db7a49f30f3886")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-gdsfmt", type=("build", "run"))
	depends_on("r-snprelate", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-piggyback", type=("build", "run"))
