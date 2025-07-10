# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpistasisga(RPackage):
	"""An R package to identify multi-snp effects in nuclear family studies using the GADGETS method

	This package runs the GADGETS method to identify epistatic effects in nuclear family studies. It also provides functions for permutation-based inference and graphical visualization of the results.
	"""
	
	homepage = "https://github.com/mnodzenski/epistasisGA"
	bioc = "epistasisGA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/epistasisGA_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/epistasisGA/epistasisGA_1.4.0.tar.gz"]

	version("1.4.0", sha256="214867cd3357037f6c094be7ef2dda4c7fb5653a84fd86b2c8354b06882ad836")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-batchtools", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
