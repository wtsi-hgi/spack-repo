# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErma(RPackage):
	"""epigenomic road map adventures

	Software and data to support epigenomic road map adventures.
	"""
	
	bioc = "erma"

	version("1.24.1", commit="84091bf5640bd699001acbf97df04bd2f004d319")
	version("1.18.0", commit="bed2908a6ebe0f28cc140d09470f1d4368ef9f2b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-homo-sapiens", type=("build", "run"))
	depends_on("r-genomicfiles@1.5.2:", type=("build", "run"))
	depends_on("r-rtracklayer@1.38.1:", type=("build", "run"))
	depends_on("r-s4vectors@0.23.18:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
