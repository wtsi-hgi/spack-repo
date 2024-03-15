# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSampleclassifierdata(RPackage):
	"""Pre-processed data for use with the sampleClassifier package

	This package contains two microarray and two RNA-seq datasets that have been preprocessed for use with the sampleClassifier package. The RNA-seq data are derived from Fagerberg et al. (2014) and the Illumina Body Map 2.0 data. The microarray data are derived from Roth et al. (2006) and Ge et al. (2005).
	"""
	
	bioc = "sampleClassifierData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/sampleClassifierData_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/sampleClassifierData/sampleClassifierData_1.26.0.tar.gz"]

	version("1.26.0", md5="941790a92cde9051601206ed162f4151")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

	# experiment