# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoxphf(RPackage):
	"""Cox Regression with Firth's Penalized Likelihood

	Implements Firth's penalized maximum likelihood bias reduction method  for Cox regression
  which has been shown to provide a solution in case of monotone likelihood (nonconvergence of likelihood function), see 
  Heinze and Schemper (2001) and Heinze and Dunkler (2008).
  The program fits profile penalized likelihood confidence intervals which were proved to outperform
  Wald confidence intervals.
	"""
	
	homepage = "https://cemsiis.meduniwien.ac.at/kb/wf/software/statistische-software/fccoxphf/"
	cran = "coxphf" 

	version("1.13.4", md5="0e3380051ab8da239a8526f24d172428")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
