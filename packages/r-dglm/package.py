# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDglm(RPackage):
	"""Double Generalized Linear Models

	Model fitting and evaluation tools for double generalized linear
    models (DGLMs). This class of models uses one generalized linear model (GLM)
    to fit the specified response and a second GLM to fit the deviance of the first
    model.
	"""
	
	cran = "dglm" 

	version("1.8.6", md5="c8b51a4793f204eff66ea43c926db19d")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
