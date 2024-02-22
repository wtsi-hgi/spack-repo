# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocationgamer(RPackage):
	"""Identification of Location Game Equilibria in Networks

	Identification of equilibrium locations in location games (Hotelling (1929) 
    <doi:10.2307/2224214>). In these games, two competing actors place
    customer-serving units in two locations simultaneously. Customers make the 
    decision to visit the location that is closest to them. The functions in 
    this package include Prim algorithm (Prim (1957) 
    <doi:10.1002/j.1538-7305.1957.tb01515.x>) to find the minimum spanning tree 
    connecting all network vertices, an implementation of Dijkstra algorithm 
    (Dijkstra (1959) <doi:10.1007/BF01386390>) to find the shortest distance and 
    path between any two vertices, a self-developed algorithm using elimination 
    of purely dominated strategies to find the equilibrium, and several plotting 
    functions.
	"""
	
	cran = "locationgamer" 

	version("0.1.0", md5="be09f0cefda7f83bcb7e67648f03fd80")

