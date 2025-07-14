# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCghcall(RPackage):
	"""Calling aberrations for array CGH tumor profiles.

	Calls aberrations for array CGH data using a six state mixture model as well as several biological concepts that are ignored by existing algorithms. Visualization of profiles is also provided.
	"""
	
	bioc = "CGHcall"

	version("2.70.0", commit="2ad9ad1ad964b93636aa178fa11b309a11160517")
	version("2.64.0", commit="b735fbdcf9a6720a28dcd0fa47b6c3c340d9ebb7")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-impute@1.8:", type=("build", "run"))
	depends_on("r-dnacopy@1.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-cghbase@1.15.1:", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
