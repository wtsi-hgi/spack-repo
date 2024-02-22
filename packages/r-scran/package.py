# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScran(RPackage):
	"""Methods for Single-Cell RNA-Seq Data Analysis.

	Implements miscellaneous functions for interpretation of single-cell
	RNA-seq data.  Methods are provided for assignment of cell cycle phase,
	detection of highly variable and significantly correlated genes,
	identification of marker genes, and other common tasks in routine
	single-cell analysis workflows."""

	bioc = "scran"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/scran_1.30.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/scran/scran_1.30.2.tar.gz"]

	version("1.30.2", md5="36f9f69d4699d050a95d6f6f971d2387")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
	depends_on("r-bluster", type=("build", "run"))
	depends_on("r-metapod", type=("build", "run"))
	depends_on("r-dqrng", type=("build", "run"))
	depends_on("r-beachmat", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
