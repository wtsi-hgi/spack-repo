# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThData(RPackage):
	"""TH's Data Archive.

	Contains data sets used in other packages Torsten Hothorn maintains."""

	cran = "TH.data"

	version("1.1-2", md5="4e6e59fee15e056be3721f7c0d4e017c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
