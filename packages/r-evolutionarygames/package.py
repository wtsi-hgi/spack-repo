# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvolutionarygames(RPackage):
	"""Important Concepts of Evolutionary Game Theory

	Evolutionary game theory applies game theory to evolving populations 
    in biology, see e.g. one of the books by Weibull (1994, ISBN:978-0262731218) 
    or by Sandholm (2010, ISBN:978-0262195874) for more details. A comprehensive 
	set of tools to illustrate the core concepts of evolutionary game theory, 
	such as evolutionary stability or various evolutionary dynamics, for teaching 
	and academic research is provided.
	"""
	
	cran = "EvolutionaryGames" 

	version("0.1.2", md5="6d3a81b67c423e6cfb3f99ad82f3211e")

	depends_on("r-desolve@1.14:", type=("build", "run"))
	depends_on("r-geometry@0.3.6:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-interp@1.0.29:", type=("build", "run"))
	depends_on("r-mass@7.3.43:", type=("build", "run"))
	depends_on("r-reshape2@1.4.2:", type=("build", "run"))
