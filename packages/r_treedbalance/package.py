# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreedbalance(RPackage):
	"""Computation of 3D Tree Imbalance

	The main goal of the R package 'treeDbalance' is to provide
    functions for the computation of several measurements of 3D node
    imbalance and their respective 3D tree imbalance indices, as well as to
    introduce the new 'phylo3D' format for rooted 3D tree objects.
    Moreover, it encompasses an example dataset of 3D models of 63 beans 
    in 'phylo3D' format. Please note that this R package was developed 
    alongside the project described in the manuscript 'Measuring 3D tree 
    imbalance of plant models using graph-theoretical approaches' by 
    M. Fischer, S. Kersting, and L. Kühn (2023) <arXiv:2307.14537>, which 
    provides precise mathematical definitions of the measurements.  
    Furthermore, the package contains several helpful functions, for example, 
    some auxiliary functions for computing the ancestors, descendants, and 
    depths of the nodes, which ensures that the computations can be done in 
    linear time.  
    Most functions of 'treeDbalance' require as input a rooted tree in the 
    'phylo3D' format, an extended 'phylo' format (as introduced in the R package
    'ape' 1.9 in November 2006). Such a 'phylo3D' object must have at least 
    two new attributes next to those required by the 'phylo' format: 
    'node.coord', the coordinates of the nodes, as well as 'edge.weight', 
    the literal weight or volume of the edges.  
    Optional attributes are 'edge.diam', the diameter of the edges, and
    'edge.length', the length of the edges. For visualization purposes one
    can also specify 'edge.type', which ranges from normal cylinder to bud
    to leaf, as well as 'edge.color' to change the color of the edge depiction.  
    This project was supported by the joint research project DIG-IT! 
    funded by the European Social Fund (ESF), reference:
    ESF/14-BM-A55-0017/19, and the Ministry of Education, Science and
    Culture of Mecklenburg-Western Pomerania, Germany, as well as by the
    the project ArtIGROW, which is a part of the WIR!-Alliance 'ArtIFARM – 
    Artificial Intelligence in Farming' funded by the German Federal Ministry 
    of Education and Research (FKZ: 03WIR4805).
	"""
	
	cran = "treeDbalance" 

	version("1.0.1", md5="9d04f0bd70daeeac89828013dc2357c3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
