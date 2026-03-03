# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROttr(RPackage):
	"""An R Autograding Extension for Otter-Grader

	
    An R autograding extension for Otter-Grader (<https://otter-grader.readthedocs.io>). It supports 
    grading R scripts, R Markdown documents, and R Jupyter Notebooks.
	"""
	
	cran = "ottr" 

	version("1.5.0", md5="6ef7445c4a200c1edd4a552731729679")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
