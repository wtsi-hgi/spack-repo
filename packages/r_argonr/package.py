# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArgonr(RPackage):
	"""R Interface to Argon HTML Design

	R wrapper around the argon HTML library.
    More at <https://demos.creative-tim.com/argon-design-system/>.
	"""
	
	homepage = "https://github.com/RinteRface/argonR"
	cran = "argonR" 

	version("0.2.0", md5="0f7da78de46df90365a1a44b94e39a5f")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
