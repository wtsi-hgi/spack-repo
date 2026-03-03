# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSclust(RPackage):
	"""R Toolbox for Unsupervised Spectral Clustering

	Toolbox containing a variety of spectral clustering tools functions. Among the tools available are the hierarchical spectral clustering algorithm, the Shi and Malik clustering algorithm, the Perona and Freeman algorithm, the non-normalized clustering, the Von Luxburg algorithm, the Partition Around Medoids clustering algorithm, a multi-level clustering algorithm, recursive clustering and the fast method for all clustering algorithm. As well as other tools needed to run these algorithms or useful for unsupervised spectral clustering. This toolbox aims to gather the main tools for unsupervised spectral classification. See <http://mawenzi.univ-littoral.fr/> for more information and documentation. 
	"""
	
	cran = "sClust" 

	version("1.0", md5="afddc5026d91a9dab3213a9eaf0aa593")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
