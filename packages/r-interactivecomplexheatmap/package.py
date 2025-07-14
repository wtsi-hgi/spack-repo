# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInteractivecomplexheatmap(RPackage):
	"""Make Interactive Complex Heatmaps

	This package can easily make heatmaps which are produced by the ComplexHeatmap package into interactive applications. It provides two types of interactivities: 1. on the interactive graphics device, and 2. on a Shiny app. It also provides functions for integrating the interactive heatmap widgets for more complex Shiny app development.
	"""
	
	homepage = "https://github.com/jokergoo/InteractiveComplexHeatmap"
	bioc = "InteractiveComplexHeatmap" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/InteractiveComplexHeatmap_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/InteractiveComplexHeatmap/InteractiveComplexHeatmap_1.10.0.tar.gz"]

    version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="774e59f097827c840e4b3455928b2e2cd7f08289d4f1ee51bb9d48fab5c11e92")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-complexheatmap@2.11:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-getoptlong", type=("build", "run"))
	depends_on("r-s4vectors@0.26.1:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-kableextra@1.3.1:", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-clisymbols", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-fontawesome", type=("build", "run"))
