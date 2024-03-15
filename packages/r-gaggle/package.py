# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaggle(RPackage):
	"""Broadcast data between R and Gaggle

	This package contains functions enabling data exchange between R and Gaggle enabled bioinformatics software, including Cytoscape, Firegoose and Gaggle Genome Browser.
	"""
	
	homepage = "http://gaggle.systemsbiology.net/docs/geese/r/"
	bioc = "gaggle" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/gaggle_1.70.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/gaggle/gaggle_1.70.0.tar.gz"]

	version("1.70.0", md5="3dc385e959f454cd56dec418800c33a6")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-rjava@0.4:", type=("build", "run"))
	depends_on("r-graph@1.10.2:", type=("build", "run"))
	depends_on("r-runit@0.4.17:", type=("build", "run"))
