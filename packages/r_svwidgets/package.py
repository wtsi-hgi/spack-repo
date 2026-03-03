# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvwidgets(RPackage):
	"""Management of GUI Widgets, Windows, and Other GUI Resources

	High level management of widgets, windows and other graphical resources.
	"""
	
	homepage = "http://www.sciviews.org/SciViews-R"
	cran = "svWidgets" 

	version("0.9-45", md5="11304c370ddb72c5f2c20d6783fd7a86")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-svmisc@0.9.68:", type=("build", "run"))
