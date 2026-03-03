# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnopa(RPackage):
	"""Analyses of Proportions using Anscombe Transform

	
    Analyses of Proportions can be performed on the Anscombe (arcsine-related) transformed  
    data. The 'ANOPA' package can analyze proportions obtained from up to 
    four factors. The factors can be within-subject or between-subject or a mix 
    of within- and between-subject. The main, omnibus analysis can be followed by
    additive decompositions into interaction effects, main effects, simple 
    effects, contrast effects, etc., mimicking precisely the logic of ANOVA. For
    that reason, we call this set of tools 'ANOPA' (Analysis of Proportion
    using Anscombe transform) to highlight its similarities with ANOVA. 
    The 'ANOPA' framework also allows plots of proportions easy to obtain 
    along with confidence intervals. Finally, effect sizes and planning statistical 
    power are easily done under this framework. Only particularity, the 'ANOPA' computes  
    F statistics which have an infinite degree of freedom on the denominator. 
    See Laurencelle and Cousineau (2023) <doi:10.3389/fpsyg.2022.1045436>.
	"""
	
	homepage = "https://dcousin3.github.io/ANOPA/"
	cran = "ANOPA" 

	version("0.1.3", md5="6c5221c549d70d170ad185bc14a0398b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-superb@0.95:", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
	depends_on("r-rrapply", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
