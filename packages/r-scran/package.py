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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scran_1.30.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scran/scran_1.30.2.tar.gz"]
    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.2", sha256="7adf3d32a8dabecc4ebe08bc076604d98a372a5330b8cef5eac8a2d63c296419")
	version("1.28.0", commit="2e542b929b231fb5bb8c40af0f6ccea97f79234d")
	version("1.26.0", commit="df66576d6958a088c38bd45e1cad9c16cbb52991")
	version("1.24.1", commit="1a83eb7c948b1dc49253080c23b26cefb3a0f3b9")
	version("1.24.0", commit="c3f9e169c4538ce827d4f14a4141571c2366cd31")

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
