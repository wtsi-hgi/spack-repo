# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwidgets2(RPackage):
	"""Rewrite of gWidgets API for Simplified GUI Construction

	Re-implementation of the 'gWidgets' API. The API is defined in this
    package. A second, toolkit-specific package is required to use it. At this point only 'gWidgets2tcltk' is viable.
	"""
	
	homepage = "https://github.com/gWidgets3/gWidgets2"
	cran = "gWidgets2" 

	version("1.0-9", md5="07efb4b1520da36a7cc0877fc814c595", url="https://cran.r-project.org/src/contrib/gWidgets2_1.0-9.tar.gz")

	depends_on("r-digest", type=("build", "run"))
