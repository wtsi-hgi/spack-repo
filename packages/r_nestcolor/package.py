# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNestcolor(RPackage):
	"""Colors for NEST Graphs

	Clinical reporting figures require to use consistent colors and
  configurations. As a part of the Roche open-source clinical reporting project,
  namely the NEST project, the 'nestcolor' package specifies the color code and
  default theme with specifying 'ggplot2' theme parameters. Users can easily customize
  color and theme settings before using the reset of NEST packages to ensure consistent
  settings in both static and interactive output at the downstream.
	"""
	
	homepage = "https://github.com/insightsengineering/nestcolor/"
	cran = "nestcolor" 

	version("0.1.2", md5="2d7f81bc6fa3d835acf858a9b68d99aa")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
