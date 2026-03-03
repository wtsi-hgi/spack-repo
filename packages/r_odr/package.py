# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROdr(RPackage):
	"""Optimal Design and Statistical Power for Experimental Studies
Investigating Main, Mediation, and Moderation Effects

	Calculate the optimal sample size allocation that 
    produces the highest statistical power for experimental 
    studies under a budget constraint, and
    perform power analyses with and without accommodating 
    cost structures of sampling. The designs cover single-level 
    and multilevel experiments detecting main, mediation, 
    and moderation effects (and some combinations). 
    The references for the proposed methods include: 
    (1) Shen, Z., & Kelcey, B. (2020). 
    Optimal sample allocation under unequal costs in 
    cluster-randomized trials.
    Journal of Educational and Behavioral Statistics, 45(4): 446-474.
        <doi:10.3102/1076998620912418>.
    (2) Shen, Z., & Kelcey, B. (2022b). Optimal sample allocation for
    three-level multisite cluster-randomized trials. 
    Journal of Research on Educational Effectiveness, 15 (1), 130-150.
    <doi:10.1080/19345747.2021.1953200>.
    (3) Shen, Z., & Kelcey, B. (2022a). Optimal sample allocation in
    multisite randomized trials. The Journal of Experimental Education.
    <doi:10.1080/00220973.2020.1830361>.
    (4) Champely, S. (2020). pwr: Basic functions for power analysis 
    (Version 1.3-0) [Software]. Available from 
    <https://CRAN.R-project.org/package=pwr>.
	"""
	
	cran = "odr" 

	version("1.4.4", md5="0189ebaa3cb19084ea31eabadc8523ae")

	depends_on("r@3.3:", type=("build", "run"))
