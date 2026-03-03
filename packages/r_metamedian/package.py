# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetamedian(RPackage):
	"""Meta-Analysis of Medians

	Implements several methods to meta-analyze studies that report the 
    sample median of the outcome. When the primary studies are one-group 
    studies, the methods of McGrath et al. (2019) <doi:10.1002/sim.8013> and 
    Ozturk and Balakrishnan (2020) <doi:10.1002/sim.8738> can be applied to 
    estimate the pooled median. In the two-group context, the 
    methods of McGrath et al. (2020a) <doi:10.1002/bimj.201900036> can be 
    applied to estimate the pooled difference of medians across groups. 
    Additionally, a number of methods (e.g., McGrath et al. (2020b) 
    <doi:10.1177/0962280219889080>, Cai et al. (2021) 
    <doi:10.1177/09622802211047348>, and McGrath et al. (2023) 
    <doi:10.1177/09622802221139233>) are implemented to estimate 
    study-specific (difference of) means and their standard errors in order to 
    estimate the pooled (difference of) means. See McGrath et al. (in press) 
    <doi:10.1002/jrsm.1686> for a detailed guide on using the package.
	"""
	
	homepage = "https://github.com/stmcg/metamedian"
	cran = "metamedian" 

	version("1.1.1", md5="3a9634abaff5766f1cc9cf90280b7212")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-estmeansd", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-metablue", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
