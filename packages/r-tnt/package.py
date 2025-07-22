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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TnT_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TnT/TnT_1.24.0.tar.gz"]

	version("1.24.0", sha256="657bc90384196dc12a86b8b4628396c1d6cdacf5ce6b3977069ac6066f169bf8")

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
