# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcrnatools(RPackage):
	"""An R toolkit for non-coding RNA

	ncRNAtools provides a set of basic tools for handling and analyzing non-coding RNAs. These include tools to access the RNAcentral database and to predict and visualize the secondary structure of non-coding RNAs. The package also provides tools to read, write and interconvert the file formats most commonly used for representing such secondary structures.
	"""
	
	bioc = "ncRNAtools" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ncRNAtools_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ncRNAtools/ncRNAtools_1.12.0.tar.gz"]

	version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="3af6a08be940b38404809590cc357ec6b703e27023d3212161da833d5a95538f")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
