# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeal(RPackage):
	"""Learning Bayesian Networks with Mixed Variables

	Bayesian networks with continuous and/or discrete
        variables can be learned and compared from data. The method is described in Boettcher and Dethlefsen (2003), <doi:10.18637/jss.v008.i20>.
	"""
	
	cran = "deal" 

	version("1.2-42", md5="1894ea7778147ae4f8eef19d8c191670")

	depends_on("r@2:", type=("build", "run"))
