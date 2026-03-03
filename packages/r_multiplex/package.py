# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiplex(RPackage):
	"""Algebraic Tools for the Analysis of Multiple Social Networks

	Algebraic procedures for analyses of multiple social networks are delivered with this 
	    package as described in Ostoic (2020) <DOI:10.18637/jss.v092.i11>. 'multiplex' makes 
	    possible, among other things, to create and manipulate multiplex, multimode, and 
	    multilevel network data with different formats. Effective ways are available to treat 
	    multiple networks with routines that combine algebraic systems like the partially ordered 
	    semigroup with decomposition procedures or semiring structures with the relational 
	    bundles occurring in different types of multivariate networks. 'multiplex' provides also 
	    an algebraic approach for affiliation networks through Galois derivations between families 
	    of the pairs of subsets in the two domains of the network with visualization options.
	"""
	
	homepage = "https://github.com/mplex/multiplex/"
	cran = "multiplex" 

	version("3.1.1", md5="7ff04c2f84582eee8937fba507c0d670")

	depends_on("r@4.2:", type=("build", "run"))
