# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPagenum(RPackage):
	"""Put Page Numbers on Graphics

	A simple way to add page numbers to base/ggplot/lattice graphics.
	"""
	
	homepage = "https://kwstat.github.io/pagenum/"
	cran = "pagenum" 

	version("1.2", md5="e7c0f18a397782133a41b9314ce8ca5e")

