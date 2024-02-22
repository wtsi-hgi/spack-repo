# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreebalance(RPackage):
	"""Computation of Tree (Im)Balance Indices

	The aim of the 'R' package 'treebalance' is to provide functions for the computation of 
    a large variety of (im)balance indices for rooted trees. The package accompanies the book 
    ''Tree balance indices: a comprehensive survey'' by M. Fischer, L. Herbst, S. Kersting, 
    L. Kuehn and K. Wicke (2023) <ISBN: 978-3-031-39799-8>, <doi:10.1007/978-3-031-39800-1>, which gives a precise definition for the terms 'balance index' and 'imbalance index' (Chapter 4)
    and provides an overview of the terminology in this manual (Chapter 2). For further information 
    on (im)balance indices, see also Fischer et al. (2021) <https://treebalance.wordpress.com>.
    Considering both established and new (im)balance indices, 'treebalance' provides (among 
    others) functions for calculating the following 18 established indices and index families: the 
    average leaf depth, the B1 and B2 index, the Colijn-Plazzotta rank, the normal, corrected, 
    quadratic and equal weights Colless index, the family of Colless-like indices, the family of 
    I-based indices, the Rogers J index, the Furnas rank, the rooted quartet index, the s-shape 
    statistic, the Sackin index, the symmetry nodes index, the total cophenetic index and the 
    variance of leaf depths. Additionally, we include 9 tree shape statistics that satisfy the 
    definition of an (im)balance index but have not been thoroughly analyzed in terms of tree 
    balance in the literature yet. These are: the total internal path length, the total path length, 
    the average vertex depth, the maximum width, the modified maximum difference in widths, the 
    maximum depth, the maximum width over maximum depth, the stairs1 and the stairs2 index. 
    As input, most functions of 'treebalance' require a rooted (phylogenetic) tree in 'phylo' format 
    (as introduced in 'ape' 1.9 in November 2006). 'phylo' is used to store (phylogenetic) trees 
    with no vertices of out-degree one. For further information on the format we kindly refer the 
    reader to E. Paradis (2012) <http://ape-package.ird.fr/misc/FormatTreeR_24Oct2012.pdf>.
	"""
	
	cran = "treebalance" 

	version("1.2.0", md5="5a3a15e26ac27d24cf0c681b4654d18a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
