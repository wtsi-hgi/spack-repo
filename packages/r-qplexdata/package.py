# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQplexdata(RPackage):
	"""Data accompanying qPLEXanalyzer package

	qPLEX-RIME and Full proteome TMT mass spectrometry datasets.
	"""
	
	bioc = "qPLEXdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/qPLEXdata_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/qPLEXdata/qPLEXdata_1.20.0.tar.gz"]

	version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="aa1fbc8cadbf3831ca182a25c8f8cb07676a5c3b305408244abf548d217fca50")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-qplexanalyzer", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-msnbase", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))

