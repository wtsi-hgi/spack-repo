# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSafestats(RPackage):
	"""Safe Anytime-Valid Inference

	Functions to design and apply tests that are anytime valid. The
  functions can be used to design hypothesis tests in the prospective/randomised
  control trial setting or in the observational/retrospective setting. The
  resulting tests remain valid under both optional stopping and optional
  continuation. The current version includes safe t-tests and safe tests of
  two proportions. For details on the theory of safe tests, see
  Grunwald, de Heide and Koolen (2019) "Safe Testing" <arXiv:1906.07801>, 
  for details on safe logrank tests see ter Schure, Perez-Ortiz, Ly and Grunwald
  (2020) "The Safe Logrank Test: Error Control under Continuous Monitoring with 
  Unlimited Horizon" <arXiv:2011.06931v3> and Turner, Ly and Grunwald (2021)
  "Safe Tests and Always-Valid Confidence Intervals for contingency tables and 
  beyond" <arXiv:2106.02693> for details on safe contingency table tests.
	"""
	
	cran = "safestats" 

	version("0.8.7", md5="3c249055982e199f6cb9bb460cb59527")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-hypergeo@1.2.13:", type=("build", "run"))
	depends_on("r-survival@3.2.13:", type=("build", "run"))
	depends_on("r-biasedurn@1.7:", type=("build", "run"))
	depends_on("r-boot@1.3.28:", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
	depends_on("r-purrr@0.3.5:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
