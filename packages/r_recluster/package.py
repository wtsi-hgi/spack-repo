# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecluster(RPackage):
	"""Ordination Methods for the Analysis of Beta-Diversity Indices

	The analysis of different aspects of biodiversity requires specific algorithms. 
	For example, in regionalisation analyses, the high frequency of ties and zero values in 
	dissimilarity matrices produced by Beta-diversity turnover produces hierarchical 
	cluster dendrograms whose topology and bootstrap supports are affected by the order of 
	rows in the original matrix. Moreover, visualisation of biogeographical regionalisation 
	can be facilitated by a combination of hierarchical clustering and multi-dimensional 
	scaling. The recluster package provides robust techniques to visualise and analyse 
	pattern of biodiversity and to improve occurrence data for cryptic taxa. 
	Other functions 	related to recluster (e.g. the biodecrypt family) are currently 
	available in GitHub at <https://github.com/leondap/recluster>.
	"""
	
	homepage = "https://github.com/leondap/recluster"
	cran = "recluster" 

	version("2.9", md5="b70b0ec0185f428a2cc35f90f1ae16a2")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-picante", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
