# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMondrian(RPackage):
	"""A Simple Graphical Representation of the Relative Occurrence and
Co-Occurrence of Events

	The unique function of this package allows representing in a single graph the relative occurrence and co-occurrence of events measured in a sample. 
  As examples, the package was applied to describe the occurrence and co-occurrence of different species of bacterial or viral symbionts infecting arthropods at the individual level. The graphics allows determining the prevalence of each symbiont and the patterns of multiple infections (i.e. how different symbionts share or not the same individual hosts). 
  We named the package after the famous painter as the graphical output recalls Mondrian’s paintings.
	"""
	
	homepage = "https://github.com/lbbe-software/Mondrian"
	cran = "Mondrian" 

	version("1.1-1", md5="06a38a3782c30953885ba2973425112b")

	depends_on("r-rcolorbrewer", type=("build", "run"))
