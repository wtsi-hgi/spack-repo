# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLconnect(RPackage):
	"""Simple Tools to Compute Landscape Connectivity Metrics

	Provides functions to upload vectorial data and derive landscape
    connectivity metrics in habitat or matrix systems. Additionally, includes an 
    approach to assess individual patch contribution to the overall landscape 
    connectivity, enabling the prioritization of habitat patches. The computation
    of landscape connectivity and patch importance are very useful in Landscape 
    Ecology research. The metrics available are: number of components, number of 
    links, size of the largest component, mean size of components, class coincidence
    probability, landscape coincidence probability, characteristic path length, 
    expected cluster size, area-weighted flux and integral index of connectivity.
    Pascual-Hortal, L., and Saura, S. (2006) <doi:10.1007/s10980-006-0013-z>
    Urban, D., and Keitt, T. (2001) <doi:10.2307/2679983>
    Laita, A., Kotiaho, J., Monkkonen, M. (2011) <doi:10.1007/s10980-011-9620-4>.
	"""
	
	cran = "lconnect" 

	version("0.1.1", md5="7a29676821f71a5c0a2f839388332e48")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
