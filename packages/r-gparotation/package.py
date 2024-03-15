# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGparotation(RPackage):
	"""GPA Factor Rotation.

	Gradient Projection Algorithm Rotation for Factor Analysis. See
	GPArotation.Intro for more details."""

	cran = "GPArotation"

	version("2024.3-1", md5="bcb6ace2512c0c9a3019e2160a76cf64")

	depends_on("r@2:", type=("build", "run"))
