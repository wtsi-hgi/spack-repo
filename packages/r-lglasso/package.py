# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLglasso(RPackage):
	"""Longitudinal Graphical Lasso

	For high-dimensional correlated observations, this package carries out the L_1 penalized maximum likelihood 
            estimation of the precision matrix (network) and the correlation parameters. The correlated data can be 
            longitudinal data (may be irregularly spaced) with dampening correlation or clustered data with uniform correlation.  
            For the details of the algorithms, please see the paper Jie Zhou et al. Identifying Microbial Interaction Networks Based on Irregularly Spaced 
            Longitudinal 16S rRNA sequence data <doi:10.1101/2021.11.26.470159>.
	"""
	
	homepage = "https://github.com/jiezhou-2/lglasso"
	cran = "lglasso" 

	version("0.1.0", md5="a80a3a64f3a39d8e984cec159678ab70")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
