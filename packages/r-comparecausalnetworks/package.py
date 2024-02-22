# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComparecausalnetworks(RPackage):
	"""Interface to Diverse Estimation Methods of Causal Networks

	Unified interface for the estimation of causal networks, including
    the methods 'backShift' (from package 'backShift'), 'bivariateANM' (bivariate
    additive noise model), 'bivariateCAM' (bivariate causal additive model),
    'CAM' (causal additive model) (from package 'CAM'; the package is 
    temporarily unavailable on the CRAN repository; formerly available versions 
    can be obtained from the archive), 'hiddenICP' (invariant
    causal prediction with hidden variables), 'ICP' (invariant causal prediction)
    (from package 'InvariantCausalPrediction'), 'GES' (greedy equivalence
    search), 'GIES' (greedy interventional equivalence search), 'LINGAM', 'PC' (PC
    Algorithm), 'FCI' (fast causal inference), 
    'RFCI' (really fast causal inference) (all from package 'pcalg') and
    regression.
	"""
	
	homepage = "https://github.com/christinaheinze/CompareCausalNetworks"
	cran = "CompareCausalNetworks" 

	version("0.2.6.2", md5="aa4f422e88932c9fc57115d3f11457e0")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
