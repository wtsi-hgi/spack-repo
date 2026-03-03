# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REyetrackr(RPackage):
	"""Organising and Analysing Eye-Tracking Data

	A set of functions for organising and analysing datasets from
    experiments run using 'Eyelink' eye-trackers. Organising functions help
    to clean and prepare eye-tracking datasets for analysis, and mark up
    key events such as display changes and responses made by participants.
    Analysing functions help to create means for a wide range of standard
    measures (such as 'mean fixation durations'), which can then be fed into
    the appropriate statistical analyses and graphing packages as necessary.
	"""
	
	cran = "eyeTrackR" 

	version("1.0.1", md5="160b9d1ec4110bf3696c5dd427f7c89f")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
