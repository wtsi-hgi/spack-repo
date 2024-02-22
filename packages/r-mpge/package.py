# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpge(RPackage):
	"""A Two-Step Approach to Testing Overall Effect of
Gene-Environment Interaction for Multiple Phenotypes

	Interaction between a genetic variant (e.g., a single nucleotide polymorphism) and an environmental variable (e.g., physical activity) can have a shared effect on multiple phenotypes (e.g., blood lipids). We implement a two-step method to test for an overall interaction effect on multiple phenotypes. In first step, the method tests for an overall marginal genetic association between the genetic variant and the multivariate phenotype. The genetic variants which show an evidence of marginal overall genetic effect in the first step are prioritized while testing for an overall gene-environment interaction effect in the second step. Methodology is available from: A Majumdar, KS Burch, S Sankararaman, B Pasaniuc, WJ Gauderman, JS Witte (2020) <doi:10.1101/2020.07.06.190256>.
	"""
	
	homepage = "https://github.com/ArunabhaCodes/MPGE"
	cran = "MPGE" 

	version("1.0.0", md5="3c938211a2fe219894974338b6fbbd3f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
