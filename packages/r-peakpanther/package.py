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

	version("1.22.0", commit="d87335b5010d792d5d8797160e28dcdd7f05e232")
	version("1.16.1", commit="8a9ba02ea666e3616f174e855be6f3f4e3e06e48")
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
