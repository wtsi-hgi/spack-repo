# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgenoud(RPackage):
	"""R Version of GENetic Optimization Using Derivatives.

	A genetic algorithm plus derivative optimizer."""

	cran = "rgenoud"

	version("5.9-0.10", md5="0c4471232f41b2cd48f75cb1ed48c01a")

	depends_on("r@2.15:", type=("build", "run"))
