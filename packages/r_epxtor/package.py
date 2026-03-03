# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpxtor(RPackage):
	"""Import 'Epidata' XML Files '.epx'

	Import data from 'Epidata' XML files '.epx' and convert it to R data structures.
	"""
	
	cran = "epxToR" 

	version("0.4-1", md5="6d837293967595925a72b6ae930d07e8")

	depends_on("r-xml", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
