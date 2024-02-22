# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCec(RPackage):
	"""Cross-Entropy Clustering

	Splits data into Gaussian type clusters using the Cross-Entropy 
    Clustering ('CEC') method. This method allows for the simultaneous use of 
    various types of Gaussian mixture models, for performing the reduction of 
    unnecessary clusters, and for discovering new clusters by splitting them. 
    'CEC' is based on the work of Spurek, P. and Tabor, J. (2014) 
    <doi:10.1016/j.patcog.2014.03.006>.
	"""
	
	homepage = "https://github.com/swarm-lab/cec"
	cran = "CEC" 

	version("0.11.1", md5="ce8a08dfc10ed237b438f0bb9c2399c3")

