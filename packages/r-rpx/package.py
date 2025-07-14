# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpx(RPackage):
	"""R Interface to the ProteomeXchange Repository

	The rpx package implements an interface to proteomics data submitted to the ProteomeXchange consortium.
	"""
	
	homepage = "https://github.com/lgatto/rpx"
	bioc = "rpx" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rpx_2.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rpx/rpx_2.10.0.tar.gz"]

	version("2.16.0", tag="RELEASE_3_21")
	version("2.10.0", sha256="48c592e7362b3d55724ca020fabc30de7d734f24a5bc2c2abb1a32fc0ade1d0e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
