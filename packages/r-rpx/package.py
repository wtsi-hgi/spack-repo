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

	version("2.16.0", commit="9deb3090bc7f790c3d88634deab6450033f10930")
	version("2.10.0", commit="8f60536f59fc9244276bced412e302ed02de3b31")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
