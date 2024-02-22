# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRintrojs(RPackage):
	"""Wrapper for the 'Intro.js' Library

	A wrapper for the 'Intro.js' library (For more info: <https://introjs.com/>). 
  This package makes it easy to include step-by-step introductions, and clickable hints in a 'Shiny' 
  application. It supports both static introductions in the UI, and programmatic introductions from 
  the server-side. 
	"""
	
	homepage = "https://github.com/carlganz/rintrojs"
	cran = "rintrojs" 

	version("0.3.4", md5="4ddd3859335551949ed4086c8224b117")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
