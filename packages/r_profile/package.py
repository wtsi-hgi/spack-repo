# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfile(RPackage):
	"""Read, Manipulate, and Write Profiler Data

	Defines a data structure for profiler data, and methods to read and
    write from the 'Rprof' and 'pprof' file formats.
	"""
	
	homepage = "https://r-prof.github.io/profile/"
	cran = "profile" 

	version("1.0.3", md5="4b95a3839169c92223b4197da9928dce")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
