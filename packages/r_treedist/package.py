# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreedist(RPackage):
	"""Calculate and Map Distances Between Phylogenetic Trees

	Implements measures of tree similarity, including 
  information-based generalized Robinson-Foulds distances
  (Phylogenetic Information Distance, Clustering Information Distance,
  Matching Split Information Distance; Smith 2020)
  <doi:10.1093/bioinformatics/btaa614>; 
  Jaccard-Robinson-Foulds distances (Bocker et al. 2013)
  <doi:10.1007/978-3-642-40453-5_13>, 
  including the Nye et al. (2006) metric <doi:10.1093/bioinformatics/bti720>;
  the Matching Split Distance (Bogdanowicz & Giaro 2012)
  <doi:10.1109/TCBB.2011.48>;
  Maximum Agreement Subtree distances;
  the Kendall-Colijn (2016) distance <doi:10.1093/molbev/msw124>, and the
  Nearest Neighbour Interchange (NNI) distance, approximated per Li et al. 
  (1996) <doi:10.1007/3-540-61332-3_168>.
  Includes tools for visualizing mappings of tree space (Smith 2022)
  <doi:10.1093/sysbio/syab100>,
  for calculating the median of sets of trees,
  and for computing the information content of trees and splits.
	"""
	
	homepage = "https://ms609.github.io/TreeDist/"
	cran = "TreeDist" 

	version("2.7.0", md5="d98cc1d310c4824feebbc61fc1691208")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ape@5:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-phangorn@2.2.1:", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-treetools", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
