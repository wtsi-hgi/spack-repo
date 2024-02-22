# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLungexpression(RPackage):
	"""ExpressionSets for Parmigiani et al., 2004 Clinical Cancer Research paper

	Data from three large lung cancer studies provided as ExpressionSets
	"""
	
	bioc = "lungExpression" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/lungExpression_0.40.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/lungExpression/lungExpression_0.40.0.tar.gz"]

	version("0.40.0", md5="35eab717cb2e24c92faf417ad7fb9cb8")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))

	# experiment