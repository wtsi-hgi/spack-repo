# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmce(RPackage):
	"""Computer Model Calibration for Deterministic and Stochastic
Simulators

	Implements the Bayesian calibration model described
    in Pratola and Chkrebtii (2018) <DOI:10.5705/ss.202016.0403> for stochastic 
    and deterministic simulators.  Additive and multiplicative discrepancy models 
    are currently supported. See <http://www.matthewpratola.com/software> for 
    more information and examples.
	"""
	
	cran = "cmce" 

	version("0.1.0", md5="cbbde430d88c336c8371e1113d30468f")

	depends_on("r@3.2.3:", type=("build", "run"))
