# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProbmarg(RPackage):
	"""Computing Logit & Probit Predicted Probabilities & Marginal
Effects

	Computes predicted probabilities and marginal effects for 
  binary & ordinal logit and probit, (partial) generalized ordinal & 
  multinomial logit models estimated with the glm(), clm() (in the 
  'ordinal' package), and vglm() (in the 'VGAM' package) functions.
	"""
	
	cran = "ProbMarg" 

	version("1.0.1", md5="bbf6a036be8ccf7daeb2fcc59a03b60d")

	depends_on("r@3.5:", type=("build", "run"))
