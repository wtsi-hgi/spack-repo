# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFormatters(RPackage):
	"""ASCII Formatting for Values and Tables

	We provide a framework for rendering complex tables to ASCII,
    and a set of formatters for transforming values or sets of values into
    ASCII-ready display strings.
	"""
	
	homepage = "https://github.com/insightsengineering/formatters"
	cran = "formatters" 

	version("0.5.5", md5="fef69f27140342977775c2ef382bff29")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-htmltools@0.5.3:", type=("build", "run"))
