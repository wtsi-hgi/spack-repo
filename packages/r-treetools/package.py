# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreetools(RPackage):
	"""Create, Modify and Analyse Phylogenetic Trees

	Efficient implementations of functions for the creation, 
  modification and analysis of phylogenetic trees.
  Applications include:
  generation of trees with specified shapes;
  tree rearrangement;
  analysis of tree shape;
  rooting of trees and extraction of subtrees;
  calculation and depiction of split support;
  plotting the position of rogue taxa (Klopfstein & Spasojevic 2019)
  <doi:10.1371/journal.pone.0212942>;
  calculation of ancestor-descendant relationships,
  of 'stemwardness' (Asher & Smith, 2022) <doi:10.1093/sysbio/syab072>,
  and of tree balance (Mir et al. 2013) <doi:10.1016/j.mbs.2012.10.005>;
  artificial extinction (Asher & Smith, 2022) <doi:10.1093/sysbio/syab072>;
  import and export of trees from Newick, Nexus (Maddison et al. 1997)
  <doi:10.1093/sysbio/46.4.590>,
  and TNT <https://www.lillo.org.ar/phylogeny/tnt/> formats;
  and analysis of splits and cladistic information.
	"""
	
	homepage = "https://ms609.github.io/TreeTools/"
	cran = "TreeTools" 

	version("1.10.0", md5="4511cbf60e3178ea966bff71b092fb3a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ape@5.6:", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-fastmatch@1.1.3:", type=("build", "run"))
	depends_on("r-plottools", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-r-cache", type=("build", "run"))
	depends_on("r-rdpack@2.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
