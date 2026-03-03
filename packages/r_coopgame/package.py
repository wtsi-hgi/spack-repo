# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoopgame(RPackage):
	"""Important Concepts of Cooperative Game Theory

	The theory of cooperative games with transferable utility offers 
   useful insights into the way parties can share gains from cooperation and 
   secure sustainable agreements, see e.g. one of the books by Chakravarty, 
   Mitra and Sarkar (2015, ISBN:978-1107058798) or by Driessen (1988, 
   ISBN:978-9027727299) for more details. A comprehensive set of tools for 
   cooperative game theory with transferable utility is provided. Users can 
   create special families of cooperative games, like e.g. bankruptcy games, 
   cost sharing games and weighted voting games. There are functions to check 
   various game properties and to compute five different set-valued solution 
   concepts for cooperative games. A large number of point-valued solution 
   concepts is available reflecting the diverse application areas of 
   cooperative game theory. Some of these point-valued solution concepts can 
   be used to analyze weighted voting games and measure the influence of 
   individual voters within a voting body. There are routines for visualizing 
   both set-valued and point-valued solutions in the case of three or four 
   players. 
	"""
	
	cran = "CoopGame" 

	version("0.2.2", md5="6b5129158cb482db066e9467cf3391c5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-geometry@0.3.6:", type=("build", "run"))
	depends_on("r-rcdd@1.1:", type=("build", "run"))
	depends_on("r-gtools@3.5:", type=("build", "run"))
