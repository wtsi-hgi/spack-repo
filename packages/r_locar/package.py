# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocar(RPackage):
	"""A Set of Tools for Sound Localization

	A set of functions and tools to conduct acoustic source localization, as well as organize and check localization data and results. The localization functions implement the modified steered response power algorithm described by Cobos et al. (2010) <doi:10.1109/LSP.2010.2091502>.
	"""
	
	homepage = "https://github.com/rhedley/locaR"
	cran = "locaR" 

	version("0.1.2", md5="c290f90bf7850086bf2bf3e589645c8f")

	depends_on("r-seewave", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-oce", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-synchwave", type=("build", "run"))
