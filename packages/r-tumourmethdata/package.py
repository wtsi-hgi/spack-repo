# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTumourmethdata(RPackage):
	"""A Collection of DNA Methylation Datasets for Human Tumour Samples and Matching Normal Samples

	TumourMethData collects tumour methylation data from a variety of different tumour types (and also matching normal samples where available) and produced with different technologies (e.g. WGBS, RRBS and methylation arrays) and provides them as RangedSummarizedExperiments. This facilitates easy extraction of methylation data for regions of interest across different tumour types and studies.
	"""
	
	homepage = "https://github.com/richardheery/TumourMethData"
	bioc = "TumourMethData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/TumourMethData_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/TumourMethData/TumourMethData_1.0.0.tar.gz"]

	version("1.0.0", sha256="ad26c904292e57f951cb6b4f9808d0f9719b9c9faa267eb1468465510ae11380")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))

