# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBus(RPackage):
	"""Gene network reconstruction

	This package can be used to compute associations among genes (gene-networks) or between genes and some external traits (i.e. clinical).
	"""
	
	bioc = "BUS" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BUS_1.58.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BUS/BUS_1.58.0.tar.gz"]

	version("1.58.0", md5="788ab26ecf05f0df93667a7c37f564ff")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-minet", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
