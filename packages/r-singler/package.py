# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSingler(RPackage):
	"""Reference-Based Single-Cell RNA-Seq Annotation

	Performs unbiased cell type recognition from single-cell RNA sequencing data, by leveraging reference transcriptomic datasets of pure cell types to infer the cell of origin of each single cell independently.
	"""
	
	homepage = "https://github.com/LTLA/SingleR"
	bioc = "SingleR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SingleR_2.4.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SingleR/SingleR_2.4.1.tar.gz"]

	version("2.4.1", md5="ff17f8c8804598bb80a27bba33216919")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-beachmat", type=("build", "run"))
	depends_on("r-biocneighbors", type=("build", "run"))
