# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPprl(RPackage):
	"""Privacy Preserving Record Linkage

	A toolbox for deterministic, probabilistic and privacy-preserving record linkage techniques. Combines the functionality of the 'Merge ToolBox' (<https://www.record-linkage.de>) with current privacy-preserving techniques.
	"""
	
	cran = "PPRL" 

	version("0.3.8", md5="97cf5dc4b17cd459f502ab2147934768")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-settings", type=("build", "run"))
