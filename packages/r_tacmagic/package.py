# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTacmagic(RPackage):
	"""Positron Emission Tomography Time-Activity Curve Analysis

	To facilitate the analysis of positron emission tomography (PET) 
    time activity curve (TAC) data, and to encourage open science and 
    replicability, this package supports data loading and analysis of multiple 
    TAC file formats. Functions are available to analyze loaded TAC data for 
    individual participants or in batches. Major functionality includes weighted
    TAC merging by region of interest (ROI), calculating models including 
    standardized uptake value ratio (SUVR) and distribution volume ratio (DVR, 
    Logan et al. 1996 <doi:10.1097/00004647-199609000-00008>), basic plotting 
    functions and calculation of cut-off values (Aizenstein et al. 2008
    <doi:10.1001/archneur.65.11.1509>). Please see the walkthrough vignette for
    a detailed overview of 'tacmagic' functions.
	"""
	
	homepage = "https://github.com/ropensci/tacmagic"
	cran = "tacmagic" 

	version("0.3.1", md5="46e68a7ee1d36d4291674e1b8a84c259")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-r-matlab", type=("build", "run"))
