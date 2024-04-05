# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaerdata(RPackage):
	"""A collection of datasets for use with raer package

	raerdata is an ExperimentHub package that provides a collection of files useful for demostrating functionality in the raer package. Datasets include 10x genomics scRNA-seq, bulk RNA-seq, and paired whole-genome and RNA-seq data. Additionally databases of human and mouse RNA editing sites are provided.
	"""
	
	homepage = "https://github.com/rnabioco/raerdata"
	bioc = "raerdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/raerdata_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/raerdata/raerdata_1.0.0.tar.gz"]

	version("1.0.0", md5="8f250d12f89396f8d4351da5045cf22c")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))

