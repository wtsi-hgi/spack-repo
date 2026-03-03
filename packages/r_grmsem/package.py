# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrmsem(RPackage):
	"""Genetic-Relationship-Matrix Structural Equation Modelling
(GRMSEM)

	Quantitative genetics tool supporting the modelling of multivariate 
 genetic variance structures in quantitative data. It allows fitting different 
 models through multivariate genetic-relationship-matrix (GRM) 
 structural equation modelling (SEM) in unrelated individuals, 
 using a maximum likelihood approach. Specifically, 
 it combines genome-wide genotyping information, as captured by GRMs, 
 with twin-research-based SEM techniques, 
 St Pourcain et al. (2017) <doi:10.1016/j.biopsych.2017.09.020>, 
 Shapland et al. (2020) <doi:10.1101/2020.08.14.251199>.
	"""
	
	homepage = "https://CRAN.R-project.org/package=grmsem"
	cran = "grmsem" 

	version("1.1.0", md5="e877c5cf87aae8d07c6f975f4569be18")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-msm@1.6:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-optimparallel", type=("build", "run"))
