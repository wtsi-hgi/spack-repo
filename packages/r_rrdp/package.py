# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrdp(RPackage):
	"""Interface to the RDP Classifier

	Seamlessly interfaces RDP classifier (version 2.9).
	"""
	
	bioc = "rRDP" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rRDP_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rRDP/rRDP_1.36.0.tar.gz"]

	version("1.36.0", md5="1a6dbbc2c3e31aa382c312202e85ce62")

	depends_on("r-biostrings@2.26.2:", type=("build", "run"))
	depends_on("openjdk@1.4:", type=("build", "link", "run"))
