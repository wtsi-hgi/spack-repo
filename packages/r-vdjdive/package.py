# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVdjdive(RPackage):
	"""Analysis Tools for 10X V(D)J Data

	This package provides functions for handling and analyzing immune receptor repertoire data, such as produced by the CellRanger V(D)J pipeline. This includes reading the data into R, merging it with paired single-cell data, quantifying clonotype abundances, calculating diversity metrics, and producing common plots. It implements the E-M Algorithm for clonotype assignment, along with other methods, which makes use of ambiguous cells for improved quantification.
	"""
	
	homepage = "https://github.com/kstreet13/VDJdive"
	bioc = "VDJdive" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/VDJdive_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/VDJdive/VDJdive_1.4.0.tar.gz"]

	version("1.4.0", md5="938051376344953e02e510f65d156939")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
