# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadxl(RPackage):
	"""Read Excel Files.

	Import excel files into R. Supports '.xls' via the embedded 'libxls' C
	library <https://sourceforge.net/projects/libxls/> and '.xlsx' via the
	embedded 'RapidXML' C++ library <https://rapidxml.sourceforge.net>. Works
	on Windows, Mac and Linux without external dependencies."""

	cran = "readxl"

	version("1.4.3", md5="94e24bba88d6d9505261f0cdc2035d14")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cellranger", type=("build", "run"))
	depends_on("r-tibble@2.0.1:", type=("build", "run"))
	depends_on("r-cpp11@0.4:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
