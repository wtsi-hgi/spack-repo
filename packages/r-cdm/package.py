# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdm(RPackage):
	"""Cognitive Diagnosis Modeling

	
    Functions for cognitive diagnosis modeling and multidimensional item response modeling 
    for dichotomous and polytomous item responses. This package enables the estimation of 
    the DINA and DINO model (Junker & Sijtsma, 2001, <doi:10.1177/01466210122032064>),
    the multiple group (polytomous) GDINA model (de la Torre, 2011, 
    <doi:10.1007/s11336-011-9207-7>), the multiple choice DINA model (de la Torre, 2009, 
    <doi:10.1177/0146621608320523>), the general diagnostic model (GDM; von Davier, 2008, 
    <doi:10.1348/000711007X193957>), the structured latent class model (SLCA; Formann, 1992, 
    <doi:10.1080/01621459.1992.10475229>) and regularized latent class analysis 
    (Chen, Li, Liu, & Ying, 2017, <doi:10.1007/s11336-016-9545-6>). 
    See George, Robitzsch, Kiefer, Gross, and Uenlue (2017) <doi:10.18637/jss.v074.i02> 
    or Robitzsch and George (2019, <doi:10.1007/978-3-030-05584-4_26>)     
    for further details on estimation and the package structure.
    For tutorials on how to use the CDM package see 
    George and Robitzsch (2015, <doi:10.20982/tqmp.11.3.p189>) as well as
    Ravand and Robitzsch (2015).
	"""
	
	homepage = "https://github.com/alexanderrobitzsch/CDM"
	cran = "CDM" 

	version("8.2-6", md5="a032129b7536ba753cf166697ed04050")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
