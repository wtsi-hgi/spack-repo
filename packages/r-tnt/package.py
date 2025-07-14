# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTnt(RPackage):
	"""Interactive Visualization for Genomic Features

	A R interface to the TnT javascript library (https://github.com/ tntvis) to provide interactive and flexible visualization of track-based genomic data.
	"""
	
	homepage = "https://github.com/Marlin-Na/TnT"
	bioc = "TnT"

	version("1.30.0", commit="a9e21118b3623b4bba44327588de74f93641303d")
	version("1.24.0", commit="7bd5e0bed75d043369b58319b6548d8826a68fbf")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
