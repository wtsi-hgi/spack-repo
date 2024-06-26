# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpadesCore(RPackage):
	"""Utilities for Developing and Running Spatially Explicit Discrete Event
	Models.

	Provides the core framework for a discrete event system (DES) to implement
	acomplete data-to-decisions, reproducible workflow. The core DES components
	facilitate modularity, and easily enable the user to include additional
	functionality by running user-built modules. Includes conditional
	scheduling, restart after interruption, packaging of reusable modules,
	tools for developing arbitrary automated workflows, automated interweaving
	of modules of different temporal resolution, and tools for visualizing and
	understanding the DES project."""

	cran = "SpaDES.core"

	maintainers("dorton21")
	version("2.0.3", md5="c4b6b5d3396ad34039a0dd51e8c8922d")
	version("1.1.0", sha256="67af4f3f153b75a0865fde2457c5d951c2f2184d07c557879b7a8c43a6e7ad66")
	version("1.0.9", sha256="1176a41a1af334388c1b16ff4ed9a6f30007bb5ed1fa14d798c59461042537dd")
	version("1.0.5", sha256="c8b18cb5f932ea57f3cb3c7f2a302cbe7e06c875da7cd3928300d6003602f0a6")
	version("1.0.10", sha256="05e20f7d9aeef9ba68e50e993ef3027b8c85afc5e3f83f5ecaee9d1a7873e379")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-quickplot@1.0.2:", type=("build", "run"))
	depends_on("r-reproducible@2.0.9:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-data-table@1.11:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-lobstr", type=("build", "run"))
	depends_on("r-qs@0.21.1:", type=("build", "run"))
	depends_on("r-require@0.3.1:", type=("build", "run"))
	depends_on("r-terra@1.7.46:", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
