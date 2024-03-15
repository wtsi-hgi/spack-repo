# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMyvariant(RPackage):
	"""Accesses MyVariant.info variant query and annotation services

	MyVariant.info is a comprehensive aggregation of variant annotation resources. myvariant is a wrapper for querying MyVariant.info services
	"""
	
	bioc = "myvariant" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/myvariant_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/myvariant/myvariant_1.32.0.tar.gz"]

	version("1.32.0", md5="110e5245914806eb225bad404727124f")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
