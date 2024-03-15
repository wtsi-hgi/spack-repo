# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimecourse(RPackage):
	"""Statistical Analysis for Developmental Microarray Time Course Data

	Functions for data analysis and graphical displays for developmental microarray time course data.
	"""
	
	homepage = "http://www.bioconductor.org"
	bioc = "timecourse" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/timecourse_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/timecourse/timecourse_1.74.0.tar.gz"]

	version("1.74.0", md5="4a760d4bcf875bb5c0069cbef4a1af32")

	depends_on("r@2.1.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-limma@1.8.6:", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
