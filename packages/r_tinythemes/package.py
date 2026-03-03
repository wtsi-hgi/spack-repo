# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinythemes(RPackage):
	"""Lightweight Repackaging of 'Themes' for 'ggplot2'

	Themes for 'ggplot2' are a convenient way to style plots. The 'hrbrthemes' package
 contains a particularly nice one, but brings along a significant tail of dependencies. So this
 (currently experimental) package brings along just the 'theme_ipsum_rc' theme using the 'Roboto'
 'Condensed' font.  Should the font not be installed on your system, see the help in the package
 'hrbrthemes' on how to install 'Roboto Condensed'.
	"""
	
	homepage = "https://github.com/eddelbuettel/tinythemes"
	cran = "tinythemes" 

	version("0.0.2", md5="c6d2d274bc15ac5ba854fc1f21dfce96")
	version("0.0.1", md5="d1c6cad38ec3b58a0d9e5bf53cde8dd9")

	depends_on("r-ggplot2", type=("build", "run"))
