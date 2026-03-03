# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeltr(RPackage):
	"""Read Non-Rectangular Text Data

	The goal of 'meltr' is to provide a fast and friendly way to
    read non-rectangular data, such as ragged forms of csv (comma-separated
    values), tsv (tab-separated values), and fwf (fixed-width format) files.
	"""
	
	homepage = "https://r-lib.github.io/meltr/"
	cran = "meltr" 

	version("1.0.2", md5="437fc281002109391e1833545cc4c5ec")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
