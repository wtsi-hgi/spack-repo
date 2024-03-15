# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetams(RPackage):
	"""MS-based metabolomics annotation pipeline

	MS-based metabolomics data processing and compound annotation pipeline.
	"""
	
	homepage = "https://github.com/yguitton/metaMS"
	bioc = "metaMS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/metaMS_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/metaMS/metaMS_1.38.0.tar.gz"]

	version("1.38.0", md5="c26507515ab859aa42dbea4acc8cacc3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-camera", type=("build", "run"))
	depends_on("r-xcms@1.35:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
