# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForestploter(RPackage):
	"""Create Flexible Forest Plot

	Create forest plot based on the layout of the data. Confidence interval in multiple columns by groups can be done easily. Editing plot, inserting/adding text, applying theme to the plot and much more.
	"""
	
	homepage = "https://github.com/adayim/forestploter"
	cran = "forestploter" 

	version("1.1.1", md5="101d934ab7db30c9d7853ea53639bd14")

	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
