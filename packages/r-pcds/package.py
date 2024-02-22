# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcds(RPackage):
	"""Proximity Catch Digraphs and Their Applications

	Contains the functions for construction and visualization of various families 
    of the proximity catch digraphs (PCDs), see (Ceyhan (2005) ISBN:978-3-639-19063-2),
    for computing the graph invariants for testing the patterns of segregation and association against complete spatial randomness (CSR)
    or uniformity in one, two and three dimensional cases.
    The package also has tools for generating points from these spatial patterns.
    The graph invariants used in testing spatial point data are the domination number (Ceyhan (2011)
    <doi:10.1080/03610921003597211>) and arc density (Ceyhan et al. (2006) <doi:10.1016/j.csda.2005.03.002>;
    Ceyhan et al. (2007) <doi:10.1002/cjs.5550350106>). The PCD families considered are Arc-Slice PCDs,
    Proportional-Edge PCDs, and Central Similarity PCDs. 
	"""
	
	cran = "pcds" 

	version("0.1.8", md5="3bc4f6cd9e5cc2cae13292645f42af34")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
	depends_on("r-gmoip", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
