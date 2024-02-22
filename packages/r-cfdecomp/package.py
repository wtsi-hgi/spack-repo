# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCfdecomp(RPackage):
	"""Counterfactual Decomposition: MC Integration of the G-Formula

	Provides a set of functions for counterfactual decomposition (cfdecomp). The functions available in this package decompose differences in an outcome attributable to a mediating variable (or sets of mediating variables) between groups based on counterfactual (causal inference) theory. By using Monte Carlo (MC) integration (simulations based on empirical estimates from multivariable models) we provide added flexibility compared to existing (analytical) approaches, at the cost of computational power or time. The added flexibility means that we can decompose difference between groups in any outcome or and with any mediator (any variable type and distribution). See Sudharsanan & Bijlsma (2019) <doi:10.4054/MPIDR-WP-2019-004> for more information.
	"""
	
	cran = "cfdecomp" 

	version("0.4.0", md5="2969fa460d0358a5687ecac3c78b7814")

	depends_on("r@3.5:", type=("build", "run"))
