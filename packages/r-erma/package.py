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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/erma_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/erma/erma_1.18.0.tar.gz"]

	version("1.18.0", md5="38679c439fbeb31db81c90c90ba4f79d")

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
