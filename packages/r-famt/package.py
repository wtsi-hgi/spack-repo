# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFamt(RPackage):
	"""Factor Analysis for Multiple Testing (FAMT) : Simultaneous Tests
under Dependence in High-Dimensional Data

	The method proposed in this package takes into account the impact of dependence on the multiple testing procedures for high-throughput data as proposed by Friguet et al. (2009). The common information shared by all the variables is modeled by a factor analysis structure. The number of factors considered in the model is chosen to reduce the false discoveries variance in multiple tests. The model parameters are estimated thanks to an EM algorithm. Adjusted tests statistics are derived, as well as the associated p-values. The proportion of true null hypotheses (an important parameter when controlling the false discovery rate) is also estimated from the FAMT model. Graphics are proposed to interpret and describe the factors.
	"""
	
	homepage = "http://famt.free.fr/"
	cran = "FAMT" 

	version("2.6", md5="99d8ae512b56d3ae15ec9d7bce594d7d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
