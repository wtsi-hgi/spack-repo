# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterexperiment(RPackage):
	"""Compare Clusterings for Single-Cell Sequencing

	Provides functionality for running and comparing many different clusterings of single-cell sequencing data or other large mRNA Expression data sets.
	"""
	
	bioc = "clusterExperiment" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/clusterExperiment_2.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/clusterExperiment/clusterExperiment_2.22.0.tar.gz"]

	version("2.22.0", sha256="04c2d47113872ce2d325cd1e187e7ca2d011c88b8a4346b020a396736fcbdde2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.15.4:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ape@5:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-howmany", type=("build", "run"))
	depends_on("r-locfdr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-delayedarray@0.7.48:", type=("build", "run"))
	depends_on("r-hdf5array@1.7.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-zinbwave", type=("build", "run"))
	depends_on("r-phylobase", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-mbkmeans", type=("build", "run"))
