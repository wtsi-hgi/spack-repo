# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnimalhabitatnetwork(RPackage):
	"""Networks Characterising the Physical Configurations of Animal
Habitats

	Functions for generating and visualising networks for characterising the physical attributes and spatial organisations of habitat components (i.e. habitat physical configurations). The network generating algorithm first determines the X and Y coordinates of N nodes within a rectangle with a side length of L and an area of A. Then it computes the pair-wise Euclidean distance Dij between node i and j, and then a complete network with 1/Dij as link weights is constructed. Then, the algorithm removes links from the complete network with the probability as shown in the function ahn_prob(). Such link removals can make the network disconnected whereas a connected network is wanted. In such cases, the algorithm rewires one network component to its spatially nearest neighbouring component and repeat doing this until the network is connected again. Finally, it outputs an undirected network (weighted or unweighted, connected or disconnected). This package came with a manuscript on modelling the physical configurations of animal habitats using networks (in preparation).
	"""
	
	cran = "AnimalHabitatNetwork" 

	version("0.1.0", md5="d6600f270be9d7b9c899b78cf14af2cc")

	depends_on("r-igraph@1.2.4.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
