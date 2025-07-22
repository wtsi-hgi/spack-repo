# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNdexr(RPackage):
	"""NDEx R client library

	This package offers an interface to NDEx servers, e.g. the public server at http://ndexbio.org/. It can retrieve and save networks via the API. Networks are offered as RCX object and as igraph representation.
	"""
	
	homepage = "https://github.com/frankkramer-lab/ndexr"
	bioc = "ndexr" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ndexr_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ndexr/ndexr_1.24.0.tar.gz"]

    version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="728b4cd6496bb33609336185b8d3f052476fd1632768df6b5e6dd78b2592a7ea")

	depends_on("r-rcx", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
