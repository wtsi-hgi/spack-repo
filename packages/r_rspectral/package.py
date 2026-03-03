# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRspectral(RPackage):
	"""Spectral Modularity Clustering

	Implements the network clustering algorithm described in 
            Newman (2006) <doi:10.1103/PhysRevE.74.036104>. The complete 
            iterative algorithm comprises of two steps. In the first step, the 
            network is expressed in terms of its leading eigenvalue and 
            eigenvector and recursively partition into two communities. 
            Partitioning occurs if the maximum positive 
            eigenvalue is greater than the tolerance (10e-5) for the current 
            partition, and if it results in a positive contribution to the 
            Modularity.
            Given an initial separation using the leading eigen step, 'rSpectral' 
            then continues to maximise for the change in Modularity using a 
            fine-tuning step - or variate thereof. The first stage here is to 
            find the node which, when moved from one community to another, 
            gives the maximum change in Modularity. This node’s community is 
            then fixed and we repeat the process until all nodes have been moved. 
            The whole process is repeated from this new state until the change 
            in the Modularity, between the new and old state, is less than the 
            predefined tolerance.
            A slight variant of the fine-tuning step, which can improve speed 
            of the calculation, is also provided. Instead of moving each node 
            into each community in turn, we only consider moves of neighbouring 
            nodes, found in different communities, to the community of the 
            current node of interest. The two steps process is repeatedly 
            applied to each new community found, subdivided each community 
            into two new communities, until we are unable to find any division 
            that results in a positive change in Modularity. 
	"""
	
	homepage = "https://github.com/cmclean5/rSpectral"
	cran = "rSpectral" 

	version("1.0.0.10", md5="53afeed2a8faf838905764c2e67b968a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.11.2:", type=("build", "run"))
