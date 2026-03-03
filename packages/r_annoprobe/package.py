# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnoprobe(RPackage):
	"""Annotate the Gene Symbols for Probes in Expression Array

	We curated 147 of expression array, from 3 species(human,mouse,rat), 
              3 companies('Affymetrix','Illumina','Agilent'), 
              by aligning the 'Fasta' sequences of all probes of each platform to their corresponding reference genome, 
              and then annotate them to genes. 
	"""
	
	homepage = "https://github.com/jmzeng1314/AnnoProbe"
	cran = "AnnoProbe" 

	version("0.1.7", md5="305ab9259efb8596d1c149cb177ab1f8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
