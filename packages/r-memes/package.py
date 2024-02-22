# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMemes(RPackage):
	"""motif matching, comparison, and de novo discovery using the MEME Suite

	A seamless interface to the MEME Suite family of tools for motif analysis. 'memes' provides data aware utilities for using GRanges objects as entrypoints to motif analysis, data structures for examining & editing motif lists, and novel data visualizations. 'memes' functions and data structures are amenable to both base R and tidyverse workflows.
	"""
	
	homepage = "https://snystrom.github.io/memes/"
	bioc = "memes" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/memes_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/memes/memes_1.10.0.tar.gz"]

	version("1.10.0", md5="c9b7baebb9608344040a4dc38a05dea3")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-cmdfun@1.0.2:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggseqlogo", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-universalmotif@1.9.3:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-ggseqlogo", type=("build", "link", "run"))
