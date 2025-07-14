# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLimmagui(RPackage):
	"""GUI for limma Package With Two Color Microarrays

	A Graphical User Interface for differential expression analysis of two-color microarray data using the limma package.
	"""
	
	homepage = "http://bioinf.wehi.edu.au/limmaGUI/"
	bioc = "limmaGUI" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/limmaGUI_1.78.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/limmaGUI/limmaGUI_1.78.0.tar.gz"]

    version("1.84.0", tag="RELEASE_3_21")
	version("1.78.0", sha256="06a92cf6e3e39f242e033a136fbd85f9042d151fc14c736de0d00c2b07395ddf")

	depends_on("r-limma", type=("build", "run"))
	depends_on("r-r2html", type=("build", "run"))
	depends_on("r-tkrplot", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
