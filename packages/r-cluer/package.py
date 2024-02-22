# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCluer(RPackage):
	"""Cluster Evaluation

	CLUster Evaluation (CLUE) is a computational method for identifying 
              optimal number of clusters in a given time-course dataset clustered by 
              cmeans or kmeans algorithms and subsequently identify key kinases or 
              pathways from each cluster. Its implementation in R is called ClueR. 
              See README on <https://github.com/PYangLab/ClueR> for more details.
              P Yang et al. (2015) <doi:10.1371/journal.pcbi.1004403>.
	"""
	
	cran = "ClueR" 

	version("1.4.2", md5="97b01fc40e2722ad023217d5a85a3884")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
