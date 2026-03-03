# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffirt(RPackage):
	"""Diffusion IRT Models for Response and Response Time Data

	Package to fit diffusion-based IRT models to response and 
	response time data. Models are fit using marginal maximum 
	likelihood. Parameter restrictions (fixed value and equality 
	constraints) are possible. In addition, factor scores (person drift 
	rate and person boundary separation) can be estimated. Model fit 
	assessment tools are also available. The traditional diffusion model 
	can be estimated as well.
	"""
	
	cran = "diffIRT" 

	version("1.5", md5="4f2ed37de439838d7e4ffa24f30ceae9")

	depends_on("r-statmod", type=("build", "run"))
