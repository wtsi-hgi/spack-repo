# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtry(RPackage):
	"""Preprocessing Plant Trait Data

	Designed to support the application of plant trait data providing easy applicable functions
    for the basic steps of data preprocessing, e.g. data import, data exploration, selection of columns
    and rows, excluding trait data according to different attributes, geocoding, long- to wide-table
    transformation, and data export. 'rtry' was initially developed as part of the TRY R project to
    preprocess trait data received via the TRY database.
	"""
	
	homepage = "https://github.com/MPI-BGC-Functional-Biogeography/rtry"
	cran = "rtry" 

	version("1.1.0", md5="c687fb806f72561cf1f523b9b8ebe6a9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
