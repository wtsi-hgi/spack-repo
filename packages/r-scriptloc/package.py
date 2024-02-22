# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScriptloc(RPackage):
	"""Get the Location of the R Script that is Being Sourced/Executed

	Provides functions to retrieve the location of R scripts loaded through the source() function or run from the command line using the Rscript command. This functionality is analogous to the Bash shell's ${BASH_SOURCE[0]}. Users can first set the project root's path relative to the script path and then all subsequent paths relative to the root. This system ensures that all paths lead to the same location regardless of where any script is executed/loaded from without resorting to the use of setwd() at the top of the scripts.
	"""
	
	cran = "scriptloc" 

	version("1.0.0", md5="7c883f3748c814f0b2767e6018573408")

	depends_on("r@3.6:", type=("build", "run"))
