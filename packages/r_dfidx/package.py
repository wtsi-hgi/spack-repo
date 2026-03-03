# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfidx(RPackage):
	"""Indexed Data Frames

	Provides extended data frames, with a special data frame column which contains two indexes, with potentially a nesting structure.
	"""
	
	homepage = "https://cran.r-project.org/package=dfidx"
	cran = "dfidx" 

	version("0.0-5", md5="26d1468f30c4c3d98a1251f427937c63")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
