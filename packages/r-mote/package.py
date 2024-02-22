# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMote(RPackage):
	"""Effect Size and Confidence Interval Calculator

	Measure of the Effect ('MOTE') is an effect size calculator, including a 
    wide variety of effect sizes in the mean differences family (all versions of d) and 
    the variance overlap family (eta, omega, epsilon, r). 'MOTE' provides non-central 
    confidence intervals for each effect size, relevant test statistics, and output 
    for reporting in APA Style (American Psychological Association, 2010, 
    <ISBN:1433805618>) with 'LaTeX'. In research, an over-reliance on p-values 
    may conceal the fact that a study is under-powered (Halsey, Curran-Everett, 
    Vowler, & Drummond, 2015 <doi:10.1038/nmeth.3288>). A test may be statistically 
    significant, yet practically inconsequential (Fritz, Scherndl, & Kühberger, 2012 
    <doi:10.1177/0959354312436870>). Although the American Psychological Association 
    has long advocated for the inclusion of effect sizes (Wilkinson & American 
    Psychological Association Task Force on Statistical Inference, 1999 
    <doi:10.1037/0003-066X.54.8.594>), the vast majority of peer-reviewed, 
    published academic studies stop short of reporting effect sizes and confidence 
    intervals (Cumming, 2013, <doi:10.1177/0956797613504966>). 'MOTE' simplifies 
    the use and interpretation of effect sizes and confidence intervals. For more 
    information, visit <https://www.aggieerin.com/shiny-server>.
	"""
	
	cran = "MOTE" 

	version("1.0.2", md5="42f37fbab02bf85c95f1808338386e4f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mbess", type=("build", "run"))
	depends_on("r-ez", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
