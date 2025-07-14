# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistinct(RPackage):
	"""distinct: a method for differential analyses via hierarchical permutation tests

	distinct is a statistical method to perform differential testing between two or more groups of distributions; differential testing is performed via hierarchical non-parametric permutation tests on the cumulative distribution functions (cdfs) of each sample. While most methods for differential expression target differences in the mean abundance between conditions, distinct, by comparing full cdfs, identifies, both, differential patterns involving changes in the mean, as well as more subtle variations that do not involve the mean (e.g., unimodal vs. bi-modal distributions with the same mean). distinct is a general and flexible tool: due to its fully non-parametric nature, which makes no assumptions on how the data was generated, it can be applied to a variety of datasets. It is particularly suitable to perform differential state analyses on single cell data (i.e., differential analyses within sub-populations of cells), such as single cell RNA sequencing (scRNA-seq) and high-dimensional flow or mass cytometry (HDCyto) data. To use distinct one needs data from two or more groups of samples (i.e., experimental conditions), with at least 2 samples (i.e., biological replicates) per group.
	"""
	
	homepage = "https://github.com/SimoneTiberi/distinct"
	bioc = "distinct" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/distinct_1.14.5.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/distinct/distinct_1.14.5.tar.gz"]

	version("1.20.0", tag="RELEASE_3_21")
	version("1.14.5", sha256="024351f81a26bef315770d5a45066932212a580b74cdc72547d90060f01e7892")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
