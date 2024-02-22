# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbess(RPackage):
	"""The MBESS R Package

	Implements methods that are useful in designing research studies and analyzing data, with 
	particular emphasis on methods that are developed for or used within the behavioral, 
	educational, and social sciences (broadly defined). That being said, many of the methods 
	implemented within MBESS are applicable to a wide variety of disciplines. MBESS has a 
	suite of functions for a variety of related topics, such as effect sizes, confidence intervals 
	for effect sizes (including standardized effect sizes and noncentral effect sizes), sample size
	planning (from the accuracy in parameter estimation [AIPE], power analytic, equivalence, and 
	minimum-risk point estimation perspectives), mediation analysis, various properties of 
	distributions, and a variety of utility functions. MBESS (pronounced 'em-bes') was originally 
	an acronym for 'Methods for the Behavioral, Educational, and Social Sciences,' but MBESS became
	more general and now contains methods applicable and used in a wide variety of fields and is an 
	orphan acronym, in the sense that what was an acronym is now literally its name. MBESS has 
	greatly benefited from others, see <https://www3.nd.edu/~kkelley/site/MBESS.html> for a detailed 
	list of those that have contributed and other details.
	"""
	
	homepage = "https://www3.nd.edu/~kkelley/site/MBESS.html"
	cran = "MBESS" 

	version("4.9.3", md5="031d7e685970ef5d5fbddfe7ed911436")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-openmx", type=("build", "run"))
	depends_on("r-sem", type=("build", "run"))
	depends_on("r-semtools", type=("build", "run"))
