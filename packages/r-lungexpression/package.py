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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/lungExpression_0.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/lungExpression/lungExpression_0.40.0.tar.gz"]

	version("0.40.0", sha256="0c0b95295e7a81fb36574756d86827a9d1f38b74baf49fec8c00ea443545eecf")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))

