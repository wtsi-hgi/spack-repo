# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidycwl(RPackage):
	"""Tidy Common Workflow Language Tools and Workflows

	The Common Workflow Language <https://www.commonwl.org/> is an
    open standard for describing data analysis workflows. This package takes
    the raw Common Workflow Language workflows encoded in JSON or 'YAML'
    and turns the workflow elements into tidy data frames or lists.
    A graph representation for the workflow can be constructed and visualized
    with the parsed workflow inputs, outputs, and steps. Users can embed the
    visualizations in their 'Shiny' applications, and export them
    as HTML files or static images.
	"""
	
	homepage = "https://sbg.github.io/tidycwl/"
	cran = "tidycwl" 

	version("1.0.7", md5="206a1e657f57c45b9eed5e39b701d2ff")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-webshot", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
