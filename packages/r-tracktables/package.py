# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTracktables(RPackage):
	"""Build IGV tracks and HTML reports

	Methods to create complex IGV genome browser sessions and dynamic IGV reports in HTML pages.
	"""
	
	bioc = "tracktables"

	version("1.42.0", commit="81185d0d59f7d3cb86195bfb6b8fe446d68e2302")
	version("1.36.0", commit="8291a0a6aea9a55b4443a704fec74e323d265abb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-tractor-base", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
