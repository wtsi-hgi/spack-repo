# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmovie(RPackage):
	"""Some Movies to Illustrate Concepts in Statistics

	Provides movies to help students to understand statistical 
  concepts.  The 'rpanel' package  <https://cran.r-project.org/package=rpanel> 
  is used to create interactive plots that move to illustrate key statistical 
  ideas and methods.  There are movies to: visualise probability distributions
  (including user-supplied ones); illustrate sampling distributions of the
  sample mean (central limit theorem), the median, the sample maximum 
  (extremal types theorem) and (the Fisher transformation of the) 
  product moment correlation coefficient; examine the influence of an 
  individual observation in simple linear regression; illustrate key concepts 
  in statistical hypothesis testing. Also provided are dpqr functions for the 
  distribution of the Fisher transformation of the correlation coefficient 
  under sampling from a bivariate normal distribution.
	"""
	
	homepage = "https://paulnorthrop.github.io/smovie/"
	cran = "smovie" 

	version("1.1.6", md5="ec4514764ab54c3325c4cb14a595e5e4")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rpanel@1.1.3:", type=("build", "run"))
