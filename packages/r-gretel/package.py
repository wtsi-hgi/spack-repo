# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGretel(RPackage):
	"""Generalized Path Analysis for Social Networks

	The social network literature features numerous methods for assigning
    value to paths as a function of their ties. 'gretel' systemizes these approaches,
    casting them as instances of a generalized path value function indexed by 
    a penalty parameter. The package also calculates probabilistic path value and
    identifies optimal paths in either value framework. Finally, proximity 
    matrices can be generated in these frameworks that capture high-order connections 
    overlooked in primitive adjacency sociomatrices. Novel methods are described
    in Buch (2019) <https://davidbuch.github.io/analyzing-networks-with-gretel.html>. 
    More traditional methods are also implemented, as described in Yang, Knoke (2001) 
    <doi:10.1016/S0378-8733(01)00043-0>.
	"""
	
	homepage = "https://github.com/davidbuch/gretel"
	cran = "gretel" 

	version("0.0.1", md5="02b9a7a92496deea034d00ec67f4e2b6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-resistorarray@1.0.32:", type=("build", "run"))
