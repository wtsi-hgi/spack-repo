# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiassayexperiment(RPackage):
	"""Software for the integration of multi-omics experiments in Bioconductor

	MultiAssayExperiment harmonizes data management of multiple experimental assays performed on an overlapping set of specimens. It provides a familiar Bioconductor user experience by extending concepts from SummarizedExperiment, supporting an open-ended mix of standard data classes for individual assays, and allowing subsetting by genomic ranges or rownames. Facilities are provided for reshaping data into wide and long formats for adaptability to graphing and downstream analysis.
	"""
	
	homepage = "http://waldronlab.io/MultiAssayExperiment/"
	bioc = "MultiAssayExperiment" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MultiAssayExperiment_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MultiAssayExperiment/MultiAssayExperiment_1.28.0.tar.gz"]

	version("1.28.0", sha256="904dd6bb32d22d92c71de1ade4d1fd0c88e7973d01b97699a4150004abc7b036")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.3.81:", type=("build", "run"))
	depends_on("r-genomicranges@1.25.93:", type=("build", "run"))
	depends_on("r-biocbaseutils", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-s4vectors@0.23.19:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
