# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogger(RPackage):
	"""A Lightweight, Modern and Flexible Logging Utility

	Inspired by the the 'futile.logger' R package and 'logging' Python module, this utility provides a flexible and extensible way of formatting and delivering log messages with low overhead.
	"""
	
	homepage = "https://daroczig.github.io/logger/"
	cran = "logger" 

	version("0.2.2", md5="379ee674e7ca9aa384e01a338aaf1322")

