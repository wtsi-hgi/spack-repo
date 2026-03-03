# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRamclustr(RPackage):
	"""Mass Spectrometry Metabolomics Feature Clustering and
Interpretation

	A feature clustering algorithm for non-targeted mass spectrometric metabolomics data. This method is compatible with gas and liquid chromatography coupled mass spectrometry, including indiscriminant tandem mass spectrometry data <DOI: 10.1021/ac501530d>. 
	"""
	
	homepage = "https://github.com/cbroeckl/RAMClustR"
	cran = "RAMClustR" 

	version("1.3.1", md5="3082881bbab19d7c7d4046642d946a56")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-webchem", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
