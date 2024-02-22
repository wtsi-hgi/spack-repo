# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapplots(RPackage):
	"""Data Visualisation on Maps.

	Create simple maps; add sub-plots like pie plots to a map or any other
	plot; format, plot and export gridded data. The package was developed for
	displaying fisheries data but most functions can be used for more generic
	data visualisation."""

	cran = "mapplots"

	version("1.5.2", md5="d376f1fa68dd004de1fa49bf1146e465")

	depends_on("r@2.10:", type=("build", "run"))
