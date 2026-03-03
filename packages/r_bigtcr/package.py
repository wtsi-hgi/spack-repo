# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigtcr(RPackage):
	"""Nonparametric Analysis of Bivariate Gap Time with Competing
Risks

	For studying recurrent disease and death with competing
    risks, comparisons based on the well-known cumulative incidence function
    can be confounded by different prevalence rates of the competing events.
    Alternatively, comparisons of the conditional distribution of the survival
    time given the failure event type are more relevant for investigating the
    prognosis of different patterns of recurrence disease. This package implements
    a nonparametric estimator for the conditional cumulative incidence function
    and a nonparametric conditional bivariate cumulative incidence function for the
    bivariate gap times proposed in Huang et al. (2016) <doi:10.1111/biom.12494>.
	"""
	
	cran = "bigtcr" 

	version("1.1", md5="a9f9d6dda1a274ed0f53335543b1a99e")

	depends_on("r@3.4:", type=("build", "run"))
