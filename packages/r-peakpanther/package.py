# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeakpanther(RPackage):
	"""Peak Picking and Annotation of High Resolution Experiments

	An automated pipeline for the detection, integration and reporting of predefined features across a large number of mass spectrometry data files. It enables the real time annotation of multiple compounds in a single file, or the parallel annotation of multiple compounds in multiple files. A graphical user interface as well as command line functions will assist in assessing the quality of annotation and update fitting parameters until a satisfactory result is obtained.
	"""
	
	homepage = "https://github.com/phenomecentre/peakPantheR"
	bioc = "peakPantheR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/peakPantheR_1.16.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/peakPantheR/peakPantheR_1.16.1.tar.gz"]

    version("1.22.0", tag="RELEASE_3_21")
	version("1.16.1", sha256="f91d3a7f3ae883d09cfd7b134a95b884c6be8df3f94b1b07209a9dfdeb21f120")
	version("1.16.0", md5="9753434861181af826b86fbc734b5850")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
	depends_on("r-doparallel@1.0.11:", type=("build", "run"))
	depends_on("r-ggplot2@3.5:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-msnbase@2.4:", type=("build", "run"))
	depends_on("r-mzr@2.12:", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-xml@3.98.1.10:", type=("build", "run"))
	depends_on("r-minpack-lm@1.2.1:", type=("build", "run"))
	depends_on("r-scales@0.5:", type=("build", "run"))
	depends_on("r-shiny@1.0.5:", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-shinycssloaders@1:", type=("build", "run"))
	depends_on("r-dt@0.15:", type=("build", "run"))
	depends_on("r-pracma@2.2.3:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
