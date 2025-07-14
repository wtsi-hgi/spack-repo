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

	version("0.46.0", commit="5d64936b1b4889d3a01ec9b495acd1d4a75d8904")
	version("0.40.0", commit="f877a43062bf8bee4c18ba6c58d11f9ea6c41068")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))

