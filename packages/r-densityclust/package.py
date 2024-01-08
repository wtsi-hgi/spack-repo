# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RDensityclust(RPackage):
	"""Clustering by Fast Search and Find of Density Peaks

	An improved implementation (based on k-nearest neighbors) of the 
    density peak clustering algorithm, originally described by Alex Rodriguez 
    and Alessandro Laio (Science, 2014 vol. 344) <DOI: 10.1126/science.1242072>. 
    It can handle large datasets (> 100, 000 samples) very efficiently. It was 
    initially implemented by Thomas Lin Pedersen, with inputs from Sean Hughes 
    and later improved by Xiaojie Qiu to handle large datasets with kNNs.
	"""
	
	homepage = "https://github.com/thomasp85/densityClust"
	cran = "densityClust" 

	version("0.3.2", md5="4d00e650d60f200e7b04f79f2d3262c3")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
