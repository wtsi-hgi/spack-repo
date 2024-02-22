# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvsnp(RPackage):
	"""Power Calculations for SNP Studies with Censored Outcomes

	Conduct asymptotic and empirical power and sample size calculations for Single-Nucleotide Polymorphism (SNP) association studies with right censored time to event outcomes.
	"""
	
	cran = "survSNP" 

	version("0.26", md5="4dc8d4f9417199d60755d4388831633b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survival@2.36.9:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lattice@0.20.0:", type=("build", "run"))
	depends_on("r-foreach@1.3.2:", type=("build", "run"))
	depends_on("r-xtable@1.7.0:", type=("build", "run"))
	depends_on("gsl@1.14:", type=("build", "link", "run"))
