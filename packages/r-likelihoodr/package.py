# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLikelihoodr(RPackage):
	"""Likelihood Analyses for Common Statistical Tests

	A collection of functions that calculate the log likelihood 
    (support) for a range of statistical tests. Where possible the likelihood 
    function and likelihood interval for the observed data are displayed. The 
    evidential approach used here is based on the book "Likelihood" by A.W.F. 
    Edwards (1992, ISBN-13 : 978-0801844430), "Statistical Evidence" by R. 
    Royall (1997, ISBN-13 : 978-0412044113), S.N. Goodman & R. Royall 
    (2011) <doi:10.2105/AJPH.78.12.1568>, "Understanding 
    Psychology as a Science" by Z. Dienes (2008, ISBN-13 : 978-0230542310), 
    S. Glover & P. Dixon <doi:10.3758/BF03196706> 
    and others. This package accompanies "Evidence-Based Statistics" by 
    P. Cahusac (2020, ISBN-13 : 978-1119549802) 
    <doi:10.1002/9781119549833>.
	"""
	
	cran = "likelihoodR" 

	version("1.1.4", md5="3e56651f9542fece563c1f19da2b2574")

	depends_on("r-lme4", type=("build", "run"))
