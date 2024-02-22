# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGramquad(RPackage):
	"""Gram Quadrature

	Numerical integration with Gram polynomials (based on <arXiv:2106.14875> [math.NA] 28 Jun 2021, by Irfan Muhammad [School of Computer Science, University of Birmingham, UK]).
	"""
	
	homepage = "https://gitlab.com/iagogv/GramQuad"
	cran = "GramQuad" 

	version("0.1.1", md5="4a9b1b5f5281396728e2a9f3dc9e8382")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
