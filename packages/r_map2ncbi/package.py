# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMap2ncbi(RPackage):
	"""Mapping Markers to the Nearest Genomic Feature

	Allows the user to generate a list of features (gene, pseudo, RNA,
    CDS, and/or UTR) directly from NCBI database for any species with a current 
    build available. Option to save downloaded and formatted files is available, 
    and the user can prioritize the feature list based on type and assembly builds 
    present in the current build used. The user can then use the list of features 
    generated or provide a list to map a set of markers (designed for SNP markers 
    with a single base pair position available) to the closest feature based on 
    the map build. This function does require map positions of the markers to be 
    provided and the positions should be based on the build being queried through 
    NCBI. 
	"""
	
	cran = "Map2NCBI" 

	version("1.4", md5="d9ea391ce7ef8285e364ddde8287f4a7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rentrez@1.2:", type=("build", "run"))
