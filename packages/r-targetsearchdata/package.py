# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTargetsearchdata(RPackage):
	"""Example GC-MS data for TargetSearch Package

	Example files of GC-MS data for the TargetSearch Package. The package contains raw NetCDF files from a E.coli salt stress experiment, extracted peak lists, and sample metadata required for a GC-MS analysis. The raw data has been restricted for demonstration purposes.
	"""
	
	homepage = "https://github.com/acinostroza/TargetSearchData"
	bioc = "TargetSearchData"

	version("1.46.0", commit="44972fe46d4bd4ca7b420db1c894117f66c9f376")
	version("1.40.0", commit="7c06ae3d8d8fdbae8b06a52f0cfc133d4b3e57ec")


