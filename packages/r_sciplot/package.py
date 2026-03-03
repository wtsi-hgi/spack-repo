# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSciplot(RPackage):
	"""Scientific Graphing Functions for Factorial Designs

	A collection of functions that creates graphs with error
             bars for data collected from one-way or higher factorial
             designs.
	"""
	
	cran = "sciplot" 

	version("1.2-0", md5="4510ec33ecf0da8d371656de67e2db83")

