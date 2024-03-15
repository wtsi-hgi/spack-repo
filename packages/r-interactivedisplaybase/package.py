# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInteractivedisplaybase(RPackage):
	"""Base package for enabling powerful shiny web displays of Bioconductor
	objects.

	The interactiveDisplayBase package contains the the basic methods needed
	to generate interactive Shiny based display methods for Bioconductor
	objects."""

	bioc = "interactiveDisplayBase"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/interactiveDisplayBase_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/interactiveDisplayBase/interactiveDisplayBase_1.40.0.tar.gz"]

	version("1.40.0", md5="9ae8be7104ab2debe258b504bcd24e38")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
