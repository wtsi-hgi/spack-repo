# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpadesTools(RPackage):
	"""Tools for Spatially Explicit Discrete Event Simulation (SpaDES) Models.

	Provides GIS and map utilities, plus additional modeling tools for
	developing cellular automata, dynamic raster models, and agent based models
	in 'SpaDES'.  Included are various methods for spatial spreading, spatial
	agents, GIS operations, random map generation, and others. See
	'?SpaDES.tools' for an categorized overview of these additional tools."""

	cran = "SpaDES.tools"

	maintainers("dorton21")
	version("1.0.1", sha256="6b0d69c8737ff06e2cf312ff94b298b81f4c50af2efd498a124b99ed66a2be9a")
	version("1.0.0", sha256="1172b96ada7052fcaa3a113ed31eeb1b67dba70f40fa74cbb378c6e75e9235dc")
	version("0.3.10", sha256="ba4c075b534caaca413e2e97711b5475c2679d9546c8fee4a07fb2bb94d52c94")
	version("0.3.9", sha256="84dc47f55ded58746dcb943fde97fa4a4b852e1d2f45949ab1914cf8454e00f3")
	version("0.3.6", sha256="661f8ee792874e7447be78103775b63f18ec69e773a7b275dd977adb406dd3e5")
	version("2.0.5", md5="dc7c48f5bfff04fd8426ce5be39c9b30")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-checkmate@1.8.2:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-fpcompare@0.2.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reproducible@2.0.9:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
