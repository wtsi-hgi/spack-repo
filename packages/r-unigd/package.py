# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnigd(RPackage):
	"""Universal Graphics Device

	A unified R graphics backend. Render R graphics fast and easy to many common file formats.
    Provides a thread safe 'C' interface for asynchronous rendering of R graphics.
	"""
	
	homepage = "https://github.com/nx10/unigd"
	cran = "unigd" 

	version("0.1.0", md5="1674fafbd0e2d6fec077499a6859b1a1")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-systemfonts", type=("build", "run"))
	depends_on("r-cpp11@0.2.4:", type=("build", "run"))
	depends_on("libpng", type=("build", "link", "run"))
	depends_on("cairo", type=("build", "link", "run"))
	depends_on("freetype", type=("build", "link", "run"))
	depends_on("fontconfig", type=("build", "link", "run"))
