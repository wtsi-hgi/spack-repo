# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaymedr(RPackage):
	"""Computation of Bayes Factors for Common Biomedical Designs

	BAYesian inference for MEDical designs in R. Functions for the 
    computation of Bayes factors for common biomedical research designs. 
    Implemented are functions to test the equivalence (equiv_bf), 
    non-inferiority (infer_bf), and superiority (super_bf) of an experimental 
    group compared to a control group on a continuous outcome measure. Bayes 
    factors for these three tests can be computed based on raw data (x, y) or 
    summary statistics (n_x, n_y, mean_x, mean_y, sd_x, sd_y [or ci_margin 
    and ci_level]).
	"""
	
	homepage = "https://github.com/maxlinde/baymedr"
	cran = "baymedr" 

	version("0.1.1", md5="af2845a926336227776983e97485934e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
