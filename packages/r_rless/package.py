# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRless(RPackage):
	"""Leaner Style Sheets

	Converts LESS to CSS. 
    It uses V8 engine, where LESS parser is run. Functions for
    LESS text, file or folder conversion are provided.
    This work was supported by a junior grant research project by 
    Czech Science Foundation 'GACR' no. 'GJ18-04150Y'.
	"""
	
	homepage = "https://github.com/ciirc-kso/rless"
	cran = "rless" 

	version("0.1.1", md5="d41cfb7d460f53b21c64f5e5ba009ffc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
