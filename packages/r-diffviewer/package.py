# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffviewer(RPackage):
	"""HTML Widget to Show File Differences

	A HTML widget that shows differences between files
    (text, images, and data frames).
	"""
	
	homepage = "https://diffviewer.r-lib.org"
	cran = "diffviewer" 

	version("0.1.1", md5="04cd0baa042af5a4c8b11445d2ec9798")

	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
