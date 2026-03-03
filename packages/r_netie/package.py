# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetie(RPackage):
	"""Antigen T Cell Interaction Estimation

	The Bayesian hierarchical model named antigen-T cell interaction estimation is to estimate the history of the immune pressure on the evolution of the tumor clones.The model is based on the estimation result from Andrew Roth (2014) <doi:10.1038/nmeth.2883>.
	"""
	
	cran = "netie" 

	version("1.0", md5="55a98bce869809dd3adc7a386f16bc90")

	depends_on("r@3.6:", type=("build", "run"))
