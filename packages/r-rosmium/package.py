# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRosmium(RPackage):
	"""Bindings for 'Osmium Tool'

	Allows one to use 'Osmium Tool'
    (<https://osmcode.org/osmium-tool/>) from R. 'Osmium' is a
    multipurpose command line tool that enables one to manipulate and
    analyze OpenStreetMap files through several different commands.
    Currently, this package does not aim to offer functions that cover the
    entire 'Osmium' API, instead making available functions that wrap only
    a very limited set of its features.
	"""
	
	homepage = "https://ipeagit.github.io/rosmium/"
	cran = "rosmium" 

	version("0.1.0", md5="9ee042bae82edcf26b2a9b3bc65052b0")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-geojsonsf", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
