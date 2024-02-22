# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTotalcopheneticindex(RPackage):
	"""Quantify the Balance of Phylogenetic Trees

	Measures the degree of balance for a given phylogenetic tree by 
  calculating the Total Cophenetic Index.
  Reference: A. Mir, F. Rossello, L. A. Rotger (2013).
  A new balance index for phylogenetic trees.
  Math. Biosci. 241, 125-136 <doi:10.1016/j.mbs.2012.10.005>.
	"""
	
	homepage = "https://github.com/ms609/tci/"
	cran = "TotalCopheneticIndex" 

	version("2.0.1", md5="bcd298570f57aeb8616a4e5d1531370f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-treetools@1.4.5:", type=("build", "run"))
