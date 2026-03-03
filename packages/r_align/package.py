# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlign(RPackage):
	"""A Modified DTW Algorithm for Stratigraphic Time Series Alignment

	A dynamic time warping (DTW) algorithm for stratigraphic alignment,
    translated into R from the original published 'MATLAB' code by Hay et al. (2019)
    <doi:10.1130/G46019.1>. The DTW algorithm incorporates two geologically relevant
    parameters (g and edge) for augmenting the typical DTW cost matrix, allowing
    for a range of sedimentologic and chronologic conditions to be explored, as 
    well as the generation of an alignment library (as opposed to a single alignment
    solution). The g parameter relates to the relative sediment accumulation rate
    between the two time series records,  while the edge parameter relates to the 
    amount of total shared time between the records. Note that this algorithm is
    used for all DTW alignments in the Align Shiny application, detailed in Hagen
    et al. (in review).
	"""
	
	cran = "align" 

	version("0.1.0", md5="02e35f9cd6af5200ba9882c6d2a12d35")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matlab", type=("build", "run"))
