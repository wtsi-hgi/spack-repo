# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdw(RPackage):
	"""Angular Distance Weighting Interpolation

	The irregularly-spaced data are interpolated onto regular latitude-longitude grids by weighting each station according to its distance and angle from the center of a search radius.
	"""
	
	homepage = "https://github.com/PanfengZhang/adw"
	cran = "adw" 

	version("0.3.1", md5="ddb0c19612a182be8182deeee568e99f")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
