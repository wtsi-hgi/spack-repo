# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamlssData(RPackage):
	"""GAMLSS Data.

	Data used as examples in the current two books on Generalised Additive
	Models for Location Scale and Shape introduced by Rigby and Stasinopoulos
	(2005), <doi:10.1111/j.1467-9876.2005.00510.x>."""

	cran = "gamlss.data"

	version("6.0-2", md5="5b64ed3f16e92d61d45b105135ed168f")

	depends_on("r@3.5:", type=("build", "run"))
