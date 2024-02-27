# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfr(RPackage):
	"""An Alternative Display for Profiling Information

	An alternative data structure and visual rendering
    for the profiling information generated by Rprof.
	"""
	
	homepage = "https://github.com/hadley/profr"
	cran = "profr" 

	version("0.3.3", md5="9cd61ed0631ccee460558983d466cf41")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))