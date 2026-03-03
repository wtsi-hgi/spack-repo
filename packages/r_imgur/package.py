# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImgur(RPackage):
	"""An Imgur.com API Client Package

	A complete API client for the image hosting service Imgur.com, including the an imgur graphics device, enabling the easy upload and sharing of plots.
	"""
	
	homepage = "https://github.com/leeper/imguR"
	cran = "imguR" 

	version("1.0.3", md5="b3212f3e1429c3ec1693015fc0fdca79")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
