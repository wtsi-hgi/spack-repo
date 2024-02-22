# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdeoviz(RPackage):
	"""Plots data (continuous/discrete) along chromosomal ideogram

	Plots data associated with arbitrary genomic intervals along chromosomal ideogram.
	"""
	
	bioc = "IdeoViz" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/IdeoViz_1.37.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/IdeoViz/IdeoViz_1.37.0.tar.gz"]

	version("1.37.0", md5="187ebcc3f7a11124ebbe137722672ffc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
