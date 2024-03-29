# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPuniform(RPackage):
	"""Meta-Analysis Methods Correcting for Publication Bias

	Provides meta-analysis methods that correct for
    publication bias and outcome reporting bias. Four methods and a visual tool 
    are currently included in the package. The p-uniform method as described in 
    van Assen, van Aert, and Wicherts (2015) <doi:10.1037/met0000025> 
    can be used for estimating the average effect size, testing the null hypothesis 
    of no effect, and testing for publication bias using only the statistically 
    significant effect sizes of primary studies. The second method in the package 
    is the p-uniform* method as described in van Aert and van Assen (2023) 
    <doi:10.31222/osf.io/zqjr9>. This method is an extension of the p-uniform 
    method that allows for estimation of the average effect size and the 
    between-study variance in a meta-analysis, and uses both the statistically 
    significant and nonsignificant effect sizes. The third method in the package 
    is the hybrid method as described in van Aert and van Assen (2018) 
    <doi:10.3758/s13428-017-0967-6>. The hybrid method is a meta-analysis method 
    for combining a conventional study and replication/preregistered study while 
    taking into account statistical significance of the conventional study. This
    method was extended in van Aert (2023) such that it allows for the inclusion
    of multiple conventional and replication/preregistered studies. The p-uniform 
    and hybrid method are based on the statistical theory that the distribution 
    of p-values is uniform conditional on the population effect size. The fourth 
    method in the package is the Snapshot Bayesian Hybrid Meta-Analysis Method as 
    described in van Aert and van Assen (2018) <doi:10.1371/journal.pone.0175302>. 
    This method computes posterior probabilities for four true effect sizes (no, 
    small, medium, and large) based on an original study and replication while 
    taking into account publication bias in the original study. The method can 
    also be used for computing the required sample size of the replication akin 
    to power analysis in null-hypothesis significance testing. The meta-plot is 
    a visual tool for meta-analysis that provides information on the primary 
    studies in the meta-analysis, the results of the meta-analysis, and 
    characteristics of the research on the effect under study (van Assen et al., 2023). 
    Helper functions to apply the Correcting for Outcome Reporting Bias (CORB) 
    method to correct for outcome reporting bias in a meta-analysis (van Aert & 
    Wicherts, 2023).
	"""
	
	homepage = "https://github.com/RobbievanAert/puniform"
	cran = "puniform" 

	version("0.2.7", md5="15e142dffbd582ee0fecccc5da6a540f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-adgoftest@0.3:", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
