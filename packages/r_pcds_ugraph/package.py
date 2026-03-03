# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcdsUgraph(RPackage):
	"""Underlying Graphs of Proximity Catch Digraphs and Their
Applications

	Contains the functions for construction and visualization of underlying and reflexivity graphs of 
            the three families of the proximity catch digraphs (PCDs), see (Ceyhan (2005) ISBN:978-3-639-19063-2),
            and for computing the edge density of these PCD-based graphs which are then
            used for testing the patterns of segregation and association against complete spatial randomness (CSR))
            or uniformity in one and two dimensional cases. 
            The PCD families considered are Arc-Slice PCDs, Proportional-Edge (PE) PCDs (Ceyhan et al. (2006) <doi:10.1016/j.csda.2005.03.002>) 
            and Central Similarity PCDs (Ceyhan et al. (2007) <doi:10.1002/cjs.5550350106>). 
            See also (Ceyhan (2016) <doi:10.1016/j.stamet.2016.07.003>) for edge density of the underlying and 
            reflexivity graphs of PE-PCDs.
            The package also has tools for visualization of PCD-based graphs for one, two, and three dimensional data. 
	"""
	
	cran = "pcds.ugraph" 

	version("0.1.1", md5="06779fcaf6177b5738420a4114e2c092")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pcds", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
