# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnavgraphimagedata(RPackage):
	"""Image Data Used in the Loon Package Demos

	Image data used as examples in the loon R package.
	"""
	
	homepage = "http://waddella.github.io/loon/"
	cran = "RnavGraphImageData" 

	version("0.0.4", md5="5ddc4d9d6954132b2e193fe31a4e5a8e")

	depends_on("r@2.10:", type=("build", "run"))
