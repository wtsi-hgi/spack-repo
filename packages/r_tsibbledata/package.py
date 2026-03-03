# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsibbledata(RPackage):
	"""Diverse Datasets for 'tsibble'

	Provides diverse datasets in the 'tsibble' data structure. These datasets are useful for learning and demonstrating how tidy temporal data can tidied, visualised, and forecasted.
	"""
	
	homepage = "https://tsibbledata.tidyverts.org/"
	cran = "tsibbledata" 

	version("0.4.1", md5="13d5766ad8bb1cb479e7f5cf478eb59c")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-tsibble@0.9:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
