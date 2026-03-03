# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyft(RPackage):
	"""Fast and Memory Efficient Data Operations in Tidy Syntax

	Tidy syntax for 'data.table', using modification by reference whenever possible.
 This toolkit is designed for big data analysis in high-performance desktop or laptop computers.
 The syntax of the package is similar or identical to 'tidyverse'.
 It is user friendly, memory efficient and time saving. For more information,
 check its ancestor package 'tidyfst'.
	"""
	
	homepage = "https://github.com/hope-data-science/tidyft"
	cran = "tidyft" 

	version("0.5.7", md5="d22800c3af8049ae1c05fb4decec2733")

	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-fst@0.9:", type=("build", "run"))
