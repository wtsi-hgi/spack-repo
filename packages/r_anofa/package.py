# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnofa(RPackage):
	"""Analyses of Frequency Data

	
    Analyses of frequencies can be performed using an alternative test based 
    on the G statistic. The test has similar type-I error rates and power as 
    the chi-square test. However, it is based on a total statistic that can be 
    decomposed in an additive fashion into interaction effects, main effects, simple 
    effects, contrast effects, etc., mimicking precisely the logic of ANOVA. We call 
    this set of tools 'ANOFA' (Analysis of Frequency data) to highlight its 
    similarities with ANOVA. This framework also renders plots of frequencies 
    along with confidence intervals. Finally, effect sizes and planning statistical 
    power are easily done under this framework. The ANOFA is a tool that assesses 
    the significance of effects instead of the significance of parameters; as such, 
    it is more intuitive to most researchers than alternative approaches based on 
    generalized linear models. 
    See Laurencelle and Cousineau (2023) <doi:10.20982/tqmp.19.2.p173>.
	"""
	
	homepage = "https://dcousin3.github.io/ANOFA/"
	cran = "ANOFA" 

	version("0.1.3", md5="0c7950f415327c85087715b00589b8fa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rrapply@1.2.6:", type=("build", "run"))
	depends_on("r-superb@0.95:", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
