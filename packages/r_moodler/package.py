# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoodler(RPackage):
	"""Helper Functions to Work with 'Moodle' Data

	A collection of functions to connect to a 'Moodle' database, cache relevant tables locally and generate learning analytics. 
    'Moodle' is an open source Learning Management System (LMS) developed by MoodleHQ. For more information about Moodle, visit <https://moodle.org>.
	"""
	
	homepage = "https://github.com/chi2labs/moodleR"
	cran = "moodleR" 

	version("1.0.1", md5="fb33bff539f8e3febf6ad0bc9b9d2256")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-ggwordcloud", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rmariadb", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-anytime", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-rpostgres", type=("build", "run"))
