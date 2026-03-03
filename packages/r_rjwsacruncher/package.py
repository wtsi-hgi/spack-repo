# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjwsacruncher(RPackage):
	"""Interface to the 'JWSACruncher' of 'JDemetra+'

	'JDemetra+' (<https://github.com/jdemetra/jdemetra-app>) is the seasonal adjustment software officially recommended
  to the members of the European Statistical System and the European System of Central Banks. Seasonal adjustment models performed
  with 'JDemetra+' can be stored into workspaces. 'JWSACruncher' (<https://github.com/jdemetra/jwsacruncher/releases>) is a console tool that 
  re-estimates all the multi-processing defined in a workspace and to export the result. 'rjwsacruncher' allows to launch easily the 'JWSACruncher'.
	"""
	
	homepage = "https://github.com/AQLT/rjwsacruncher"
	cran = "rjwsacruncher" 

	version("0.2.0", md5="d3e411768a36136882be0b4c1a0469b8")

	depends_on("r-xml", type=("build", "run"))
