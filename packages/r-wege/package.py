# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWege(RPackage):
	"""A Metric to Rank Locations for Biodiversity Conservation

	Calculates the WEGE (Weighted Endemism including Global 
    Endangerment index) index for a particular area. Additionally it also 
    calculates rasters of KBA's (Key Biodiversity Area) criteria (A1a, A1b, A1e, 
    and B1), Weighted endemism (WE), the EDGE (Evolutionarily Distinct and
    Globally Endangered) score, Evolutionary Distinctiveness (ED) and Extinction
    risk (ER). Farooq, H., Azevedo, J., Belluardo F., Nanvonamuquitxo, C.,
    Bennett, D., Moat, J., Soares, A., Faurby, S. & Antonelli, A. (2020)
    <doi:10.1101/2020.01.17.910299>.
	"""
	
	cran = "WEGE" 

	version("0.1.0", md5="fab6272be0b76bfd48990105d29f1dea")

	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
