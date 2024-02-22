# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcoder(RPackage):
	"""Lightweight Data Structure for Recoding Categorical Data without
Factors

	A data structure and toolkit for documenting and recoding
    categorical data that can be shared in other statistical software.
	"""
	
	homepage = "https://github.com/nyuglobalties/rcoder"
	cran = "rcoder" 

	version("0.3.0", md5="762b5c7144df9091df5643d20ec0e712")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
