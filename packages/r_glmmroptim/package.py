# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmmroptim(RPackage):
	"""Approximate Optimal Experimental Designs Using Generalised
Linear Mixed Models

	Optimal design analysis algorithms for any study design that can be represented or
  modelled as a generalised linear mixed model including cluster randomised trials,
  cohort studies, spatial and temporal epidemiological studies, and split-plot designs.
  See <https://github.com/samuel-watson/glmmrBase/blob/master/README.md> for a
  detailed manual on model specification. A detailed discussion of the methods in this
  package can be found in Watson and Pan (2022) <arXiv:2207.09183>.
	"""
	
	homepage = "https://github.com/samuel-watson/glmmrOptim"
	cran = "glmmrOptim" 

	version("0.3.4", md5="a7e2b53ddd074fac56d00b239397e8bf")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-glmmrbase@0.4.6:", type=("build", "run"))
	depends_on("r-rcpp@1.0.7:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-sparsechol@0.2.1:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rminqa@0.2.2:", type=("build", "run"))
