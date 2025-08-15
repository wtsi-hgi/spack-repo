# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSna(RPackage):
	"""Tools for Social Network Analysis

	A range of tools for social network analysis, including node and graph-level indices, structural distance and covariance methods, structural equivalence detection, network regression, random graph generation, and 2D/3D network visualization.
	"""
	
	homepage = "https://statnet.org"
	cran = "sna" 

	version("2.7-2", md5="c4eb81ede668f0f8214afffba144d6cf")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-statnet-common", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))

	# R 4.5 tightened headers; some C sources in sna
	# rely on PI macro without defining it. Define PI via CFLAGS
	# to avoid build failures on modern R toolchains.
	def setup_build_environment(self, env):
		# Ensure the macro is visible to the C preprocessor used by R
		env.append_flags('PKG_CPPFLAGS', '-DPI=3.14159265358979323846')
		env.append_flags('CPPFLAGS', '-DPI=3.14159265358979323846')
