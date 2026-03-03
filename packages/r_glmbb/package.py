# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmbb(RPackage):
	"""All Hierarchical or Graphical Models for Generalized Linear
Model

	Find all hierarchical models of specified generalized linear
    model with information criterion (AIC, BIC, or AICc) within specified
    cutoff of minimum value.  Alternatively, find all such graphical models.
    Use branch and bound algorithm so we do not have to fit all models.
	"""
	
	homepage = "https://github.com/cjgeyer/glmbb"
	cran = "glmbb" 

	version("0.5-1", md5="6891168cace63919fde981c462ce46c6")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
