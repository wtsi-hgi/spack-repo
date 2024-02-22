# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapi(RPackage):
	"""Mapping Averaged Pairwise Information

	Mapping Averaged Pairwise Information (MAPI) is an
    exploratory method providing graphical representations summarizing the
    spatial variation of pairwise metrics (eg. distance, similarity
    coefficient, ...) computed between georeferenced samples.
	"""
	
	homepage = "https://www1.montpellier.inra.fr/CBGP/software/MAPI/"
	cran = "mapi" 

	version("1.0.5", md5="f9176999da6a208994a38ce9f17cb830")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-sf@0.5:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pbapply@1.3:", type=("build", "run"))
