# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwenty48(RPackage):
	"""Play a Game of 2048 in the Console

	Generates a game of 2048 that can be played in the
    console.  Supports grids of arbitrary sizes, undoing the last move,
    and resuming a game that was exited during the current session.
	"""
	
	homepage = "https://github.com/rossellhayes/twenty48"
	cran = "twenty48" 

	version("0.2.1", md5="915ede46c5fb0069b957d052ee87f622", url="https://cran.r-project.org/src/contrib/twenty48_0.2.1.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
