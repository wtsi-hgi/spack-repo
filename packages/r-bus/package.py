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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BUS_1.58.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BUS/BUS_1.58.0.tar.gz"]

	version("1.64.0", tag="RELEASE_3_21")
	version("1.58.0", sha256="1bd8eb34b1a9633bea42dd203222cfd84197f2874aeeafaef746865e68858e94")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-minet", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
