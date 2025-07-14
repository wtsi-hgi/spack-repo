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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ChromHeatMap_1.56.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ChromHeatMap/ChromHeatMap_1.56.0.tar.gz"]

	version("1.62.0", tag="RELEASE_3_21")
	version("1.56.0", sha256="7cb1aaa6405265ac4bee7ee5335fd3ba6600bc2c618c403aa3c6bedb19f1777d")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-biocgenerics@0.3.2:", type=("build", "run"))
	depends_on("r-annotate@1.20:", type=("build", "run"))
	depends_on("r-annotationdbi@1.4:", type=("build", "run"))
	depends_on("r-biobase@2.17.8:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
