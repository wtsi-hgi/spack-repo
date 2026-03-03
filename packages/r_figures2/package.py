# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFigures2(RPackage):
	"""Support for a Variety of Figure Production Tasks

	We view a figure as a collection of graphs/tables assembled on a page and optionally annotated with metadata
    (titles, headers and footers). Functions and supporting documentation are offered to streamline a variety of figure production task.
	"""
	
	homepage = "https://github.com/gcicc/figures2"
	cran = "figuRes2" 

	version("1.0.0", md5="3606218fe11f149bb801af6da4fe63ae", url="https://cran.r-project.org/src/contrib/figuRes2_1.0.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
