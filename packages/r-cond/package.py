# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCond(RPackage):
	"""Approximate Conditional Inference for Logistic and Loglinear
Models

	Higher order likelihood-based inference for logistic and 
  loglinear models.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "cond" 

	version("1.2-3.1", md5="9fb200deaaf52f009cec15f282fc5e2e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
