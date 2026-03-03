# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStratifiedmedicine(RPackage):
	"""Stratified Medicine

	A toolkit for stratified medicine, subgroup identification, and precision medicine.
    Current tools include (1) filtering models (reduce covariate space), (2) patient-level estimate
    models (counterfactual patient-level quantities, such as the conditional average treatment effect), 
    (3) subgroup identification models (find subsets of patients with similar treatment effects), 
    and (4) treatment effect estimation and inference (for the overall population and discovered 
    subgroups). These tools can be customized and are directly used in PRISM 
    (patient response identifiers for stratified medicine; Jemielita and Mehrotra 2019
    <arXiv:1912.03337>. This package is in beta and will be continually updated.
	"""
	
	homepage = "https://github.com/thomasjemielita/StratifiedMedicine"
	cran = "StratifiedMedicine" 

	version("1.0.5", md5="c67994139589c1ef2395c52b3d34975c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggparty", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
