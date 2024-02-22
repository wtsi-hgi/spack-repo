# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMutossgui(RPackage):
	"""A Graphical User Interface for the MuToss Project

	The mutossGUI package provides a graphical user interface for the MuToss Project.
	"""
	
	homepage = "http://mutoss.r-forge.r-project.org/"
	cran = "mutossGUI" 

	version("0.1-11", md5="be1e359166183f4838c5ab44c3bbdd1e")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-mutoss@0.1.6:", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rjava@0.8.0:", type=("build", "run"))
	depends_on("r-javagd@0.5.2:", type=("build", "run"))
	depends_on("r-commonjavajars@1.0.5:", type=("build", "run"))
	depends_on("r-jgr", type=("build", "run"))
	depends_on("openjdk@5:", type=("build", "link", "run"))
