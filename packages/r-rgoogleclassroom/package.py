# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgoogleclassroom(RPackage):
	"""API Wrapper for Google Classroom and Google Forms

	This is a Google Forms and Google Classroom API Wrapper for R for managing Google Classrooms from R. The documentation for these APIs is here <https://developers.google.com/forms/api/guides> .
	"""
	
	homepage = "https://github.com/datatrail-jhu/rgoogleclassroom"
	cran = "rgoogleclassroom" 

	version("0.9.1", md5="5aa73c7cc366e37252214b1d5f46dc3f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-attempt", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-ottrpal", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
