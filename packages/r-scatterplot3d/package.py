# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScatterplot3d(RPackage):
	"""3D Scatter Plot.

	Plots a three dimensional (3D) point cloud."""

	cran = "scatterplot3d"

	version("0.3-44", md5="0acaab2e9eba4ece27e1444f769d006b")

	depends_on("r@2.7:", type=("build", "run"))
