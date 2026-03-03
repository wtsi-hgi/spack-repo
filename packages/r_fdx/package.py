# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdx(RPackage):
	"""False Discovery Exceedance Controlling Multiple Testing
Procedures

	Multiple testing procedures for heterogeneous and discrete tests as described in Döhler and Roquain (2019) <arXiv:1912.04607v1>. The main algorithms of the paper are available as continuous, discrete and weighted versions.
	"""
	
	homepage = "https://github.com/DISOhda/FDX"
	cran = "FDX" 

	version("1.0.6", md5="5e66d22fea641f8d2648f4e68864927b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-discretefdr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-poissonbinomial", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
