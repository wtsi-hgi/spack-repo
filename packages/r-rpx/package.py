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

	version("2.10.0", md5="7e3f2004892b6fb40746c0dcdd990a43")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
