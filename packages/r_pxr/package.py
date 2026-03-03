# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPxr(RPackage):
	"""PC-Axis with R

	Provides a set of functions for reading and writing PC-Axis files, used by different statistical organizations around the globe for data dissemination.
	"""
	
	homepage = "https://github.com/cjgb/pxR"
	cran = "pxR" 

	version("0.42.7", md5="17282c2c8c110ad9a4bb1d9c6b8c0fa3")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
