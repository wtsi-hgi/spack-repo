# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVoss(RPackage):
	"""Generic Voss Algorithm (Random Sequential Additions)

	Generating realizations of a fractal Brownian function on uniform 1D & 2D grid with classic and generic versions of the Voss algorithm (random sequential additions).
	"""
	
	cran = "Voss" 

	version("0.1.5", md5="630be4776c89d524391d491a6b966e1f")

	depends_on("r-fields", type=("build", "run"))
