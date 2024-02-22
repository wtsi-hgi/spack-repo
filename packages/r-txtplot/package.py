# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxtplot(RPackage):
	"""Text Based Plots

	Provides functions to produce rudimentary ascii graphics
        directly in the terminal window. Provides a basic plotting
        function (and equivalents of curve, density, acf and barplot)
        as well as boxplot and image functions.
	"""
	
	cran = "txtplot" 

	version("1.0-4", md5="d7687f760ee5d42ab94ba4c6c13d5572")

