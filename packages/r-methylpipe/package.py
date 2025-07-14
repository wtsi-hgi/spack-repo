# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylpipe(RPackage):
	"""Base resolution DNA methylation data analysis

	Memory efficient analysis of base resolution DNA methylation data in both the CpG and non-CpG sequence context. Integration of DNA methylation data derived from any methodology providing base- or low-resolution data.
	"""
	
	bioc = "methylPipe"

	version("1.42.1", commit="9671cbf10b4cb456d22d2e8eee2fc4c025844a28")
	version("1.36.0", commit="eac279037142111c23ce24dfaa2145552c95d30e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment@0.2:", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
