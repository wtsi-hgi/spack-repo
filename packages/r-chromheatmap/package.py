# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChromheatmap(RPackage):
	"""Heat map plotting by genome coordinate

	The ChromHeatMap package can be used to plot genome-wide data (e.g. expression, CGH, SNP) along each strand of a given chromosome as a heat map. The generated heat map can be used to interactively identify probes and genes of interest.
	"""
	
	bioc = "ChromHeatMap" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ChromHeatMap_1.56.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ChromHeatMap/ChromHeatMap_1.56.0.tar.gz"]

	version("1.56.0", md5="ee08133257bb6da21d100e03fd720323")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-biocgenerics@0.3.2:", type=("build", "run"))
	depends_on("r-annotate@1.20:", type=("build", "run"))
	depends_on("r-annotationdbi@1.4:", type=("build", "run"))
	depends_on("r-biobase@2.17.8:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
