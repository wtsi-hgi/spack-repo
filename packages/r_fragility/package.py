# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFragility(RPackage):
	"""Assessing and Visualizing Fragility of Clinical Results with
Binary Outcomes

	A collection of user-friendly functions for assessing and visualizing fragility of individual studies (Walsh et al., 2014 <doi:10.1016/j.jclinepi.2013.10.019>; Lin, 2021 <doi:10.1111/jep.13428>), conventional pairwise meta-analyses (Atal et al., 2019 <doi:10.1016/j.jclinepi.2019.03.012>), and network meta-analyses of multiple treatments with binary outcomes (Xing et al., 2020 <doi:10.1016/j.jclinepi.2020.07.003>). The included functions are designed to: 1) calculate the fragility index (i.e., the minimal event status modifications that can alter the significance or non-significance of the original result) and fragility quotient (i.e., fragility index divided by sample size) at a specific significance level; 2) give the cases of event status modifications for altering the result's significance or non-significance and visualize these cases; 3) visualize the trend of statistical significance as event status is modified; 4) efficiently derive fragility indexes and fragility quotients at multiple significance levels, and visualize the relationship between these fragility measures against the significance levels; and 5) calculate fragility indexes and fragility quotients of multiple datasets (e.g., a collection of clinical trials or meta-analyses) and produce plots of their overall distributions. The outputs from these functions may inform the robustness of clinical results in terms of statistical significance and aid the interpretation of fragility measures. The usage of this package is detailed in Lin and Chu (2022 <doi:10.1371/journal.pone.0268754>).
	"""
	
	cran = "fragility" 

	version("1.4", md5="7c1e59ad9e743583dd757c6f69f2949e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-metafor@2.0.0:", type=("build", "run"))
	depends_on("r-netmeta@1.0.0:", type=("build", "run"))
	depends_on("r-plotrix@3.7.5:", type=("build", "run"))
