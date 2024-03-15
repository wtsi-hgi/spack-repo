# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraph4lg(RPackage):
	"""Build Graphs for Landscape Genetics Analysis

	Build graphs for landscape genetics analysis. This set of 
	functions can be used to import and convert spatial and genetic data 
	initially in different formats, import landscape graphs created with 
	'GRAPHAB' software (Foltete et al., 2012) <doi:10.1016/j.envsoft.2012.07.002>, 
	make diagnosis plots of isolation by distance relationships in order to 
	choose how to build genetic graphs, create graphs with a large range of 
	pruning methods, weight their links with several genetic distances, plot 
	and analyse graphs,	compare them with other graphs. It uses functions from 
	other packages such as 'adegenet' 
	(Jombart, 2008) <doi:10.1093/bioinformatics/btn129> and 'igraph' (Csardi
	et Nepusz, 2006) <https://igraph.org/>. It also implements methods 
	commonly used in landscape genetics to create graphs, described by Dyer et 
	Nason (2004) <doi:10.1111/j.1365-294X.2004.02177.x> and Greenbaum et 
	Fefferman (2017) <doi:10.1111/mec.14059>, and to analyse distance data 
	(van Strien et al., 2015) <doi:10.1038/hdy.2014.62>.
	"""
	
	cran = "graph4lg" 

	version("1.8.0", md5="1c5317841db3e8de616e4fe01f7eeb84")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-adegenet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-linnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-pegas", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-hierfstat", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-gdistance", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-ecodist", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
