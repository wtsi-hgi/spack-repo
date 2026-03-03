# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFivethirtyeight(RPackage):
	"""Data and Code Behind the Stories and Interactives at
'FiveThirtyEight'

	Datasets and code published by the data journalism website 
    'FiveThirtyEight' available at <https://github.com/fivethirtyeight/data>. 
    Note that while we received guidance from editors at 'FiveThirtyEight', this 
    package is not officially published by 'FiveThirtyEight'.
	"""
	
	homepage = "https://github.com/rudeboybert/fivethirtyeight"
	cran = "fivethirtyeight" 

	version("0.6.2", md5="f4a7a6c3d6635affcfe437d85b827652")

	depends_on("r@3.2.4:", type=("build", "run"))
