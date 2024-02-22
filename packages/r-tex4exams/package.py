# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTex4exams(RPackage):
	"""Generating 'Sweave' Code for 'R/exams' Questions in Mathematics

	When using the R package  'exams'  to write mathematics questions in 'Sweave' files, the output of a lot of R functions need to be adjusted for display in mathematical formulas. Specifically, the functions were accumulated when writing questions for the  topics of the mathematics courses College Algebra, Precalculus, Calculus, Differential Equations, Introduction to Probability, and Linear Algebra.  The output of the developed functions can be used in 'Sweave' files. 
	"""
	
	cran = "Tex4exams" 

	version("0.1.2", md5="50d5b872aa1e4df2121a11dac96bac4c")

	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-fractional", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
