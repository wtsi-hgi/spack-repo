# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcglm(RPackage):
	"""Information Criteria for Generalized Linear Regression

	Calculate various information criteria in literature for "lm" and "glm" objects.
	"""
	
	cran = "ICglm" 

	version("0.1.0", md5="bd53430488aaed5db925e2dc92978cfd")

	depends_on("r-matrix", type=("build", "run"))
