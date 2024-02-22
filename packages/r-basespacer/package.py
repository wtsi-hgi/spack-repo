# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasespacer(RPackage):
	"""R SDK for BaseSpace RESTful API

	A rich R interface to Illumina's BaseSpace cloud computing environment, enabling the fast development of data analysis and visualisation tools.
	"""
	
	bioc = "BaseSpaceR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BaseSpaceR_1.46.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BaseSpaceR/BaseSpaceR_1.46.0.tar.gz"]

	version("1.46.0", md5="b141511c6e978d4f26c8ec4c42c078c2")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
