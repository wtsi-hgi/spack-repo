# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocalcontrol(RPackage):
	"""Nonparametric Methods for Generating High Quality Comparative
Effectiveness Evidence

	Implements novel nonparametric approaches to address
    biases and confounding when comparing treatments or exposures in
    observational studies of outcomes. While designed and appropriate for use
    in studies involving medicine and the life sciences, the package can be
    used in other situations involving outcomes with multiple confounders.
    The package implements a family of methods for non-parametric bias correction
    when comparing treatments in observational studies, including survival
    analysis settings, where competing risks and/or censoring may be present.
    The approach extends to bias-corrected personalized predictions of treatment
    outcome differences, and analysis of heterogeneity of treatment effect-sizes
    across patient subgroups. For further details, please see: 
    Lauve NR, Nelson SJ, Young SS, Obenchain RL, Lambert CG. LocalControl:
    An R Package for Comparative Safety and Effectiveness Research.
    Journal of Statistical Software. 2020. p. 1–32. Available from <doi:10.18637/jss.v096.i04>.
	"""
	
	cran = "LocalControl" 

	version("1.1.3", md5="f2e772e084ecc6ed5a0f188112c22767")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gss", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
