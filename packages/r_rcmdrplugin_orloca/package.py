# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginOrloca(RPackage):
	"""A GUI for Planar Location Problems

	A GUI for the orloca package is provided as a Rcmdr plug-in. The package deals with continuos planar location problems.
	"""
	
	homepage = "http://knuth.uca.es/orloca/"
	cran = "RcmdrPlugin.orloca" 

	version("4.8.2", md5="883067cbb7651e54c99aa93e6b852861")

	depends_on("r-orloca@4.6:", type=("build", "run"))
	depends_on("r-orloca-es@4.6:", type=("build", "run"))
	depends_on("r-rcmdr", type=("build", "run"))
