# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQgshiny(RPackage):
	"""A 'shiny' Application for Active Learning Instruction in
Introductory Quantitative Genetics

	A 'shiny' application for teaching introductory quantitative genetics
    and plant breeding through interactive simulations. The application relies on 
    established plant breeding and quantitative genetic theory found in 
    Falconer and Mackay (1996, ISBN:0582243025) and Bernardo (2010, ISBN:978-0972072427).
	"""
	
	cran = "qgshiny" 

	version("0.1.0", md5="a56a3399f6039ae94f2c5fea66e4225e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
