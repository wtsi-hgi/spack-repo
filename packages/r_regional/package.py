# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegional(RPackage):
	"""Intra- and Inter-Regional Similarity

	Calculates intra-regional and inter-regional similarities based on user-provided
    spatial vector objects (regions) and spatial raster objects (cells with values).
    Implemented metrics include inhomogeneity, isolation 
    (Haralick and Shapiro (1985) <doi:10.1016/S0734-189X(85)90153-7>, 
    Jasiewicz et al. (2018) <doi:10.1016/j.cageo.2018.06.003>), 
    and distinction (Nowosad (2021) <doi:10.1080/13658816.2021.1893324>).
	"""
	
	cran = "regional" 

	version("0.3.3", md5="ede26dbf5d76b1f9d8d23d0ff88adbb0")

	depends_on("r-philentropy@0.6:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
