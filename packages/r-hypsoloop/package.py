# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHypsoloop(RPackage):
	"""A Tool Used to Conduct Hypsometric Analysis of a Watershed

	Functions for generating tables required for drawing and calculating hypsometric curves and hypsometric integrals.
    These functions accept as input the DEM of the region of interest (your watershed) and a spatial data frame file specifying delineation of sub-catchments within the watershed.
    They then generate output in the form of PNG images and HTML files contained in a folder named "HYPSO_OUTPUT" created in the current directory.
    S. K. Sharma, S. Gajbhiye, et al. (2018) <doi:10.1007/978-981-10-5801-1_19>.
    Omvir Singh, A. Sarangi, and Milap C. Sharma (2006) <doi:10.1007/s11269-008-9242-z>.
    James A. Vanderwaal and Herbert Ssegane (2013) <doi:10.1111/jawr.12089>.
	"""
	
	cran = "hypsoLoop" 

	version("0.2.0", md5="972b49d91f560691c1b2275d37a86c95")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-polynomf", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sjplot", type=("build", "run"))
