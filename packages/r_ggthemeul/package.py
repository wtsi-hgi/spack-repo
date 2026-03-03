# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgthemeul(RPackage):
	"""A 'ggplot' Theme for University of Ljubljana

	Designed to customize 'ggplot' graphics according to the institutional identity of the University of Ljubljana. 
	"""
	
	cran = "ggthemeUL" 

	version("0.1.3", md5="02660569ea55dc1e52ef71bc176946eb")

	depends_on("r-ggplot2", type=("build", "run"))
