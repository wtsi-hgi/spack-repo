# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgsoccer(RPackage):
	"""Plot Soccer Event Data

	The 'ggplot2' package provides a powerful set of tools
  for visualising and investigating data. The 'ggsoccer' package provides a
  set of functions for elegantly displaying and exploring soccer event data
  with 'ggplot2'. Providing extensible layers and themes, it is designed to
  work smoothly with a variety of popular sports data providers.
	"""
	
	homepage = "https://torvaney.github.io/ggsoccer/"
	cran = "ggsoccer" 

	version("0.1.7", md5="6054f00bce28d6251c280550d3c944cf")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
