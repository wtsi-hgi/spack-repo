# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZoomgroupstats(RPackage):
	"""Analyze Text, Audio, and Video from 'Zoom' Meetings

	Provides utilities for processing and analyzing the files that are exported from a recorded 'Zoom' Meeting. This includes analyzing data captured through video cameras and microphones, the text-based chat, and meta-data. You can analyze aspects of the conversation among meeting participants and their emotional expressions throughout the meeting.
	"""
	
	homepage = "http://zoomgroupstats.org"
	cran = "zoomGroupStats" 

	version("0.1.0", md5="778848d690e8ca81eabe3ad5fe7b9610")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-paws", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-syuzhet", type=("build", "run"))
