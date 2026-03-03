# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobastrda(RPackage):
	"""Interpolation Grids for Packages of the 'RobASt' - Family of
Packages

	Includes 'sysdata.rda' file for packages of the 'RobASt' - family of packages; is
            currently used by package 'RobExtremes' only.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/robast/"
	cran = "RobAStRDA" 

	version("1.2.1", md5="e4877a799ac6626303c4c8853d47c969")

	depends_on("r@3.5:", type=("build", "run"))
