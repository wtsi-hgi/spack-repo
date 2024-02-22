# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REstmeansd(RPackage):
	"""Estimating the Sample Mean and Standard Deviation from Commonly
Reported Quantiles in Meta-Analysis

	Implements the methods of McGrath et al. (2020) 
    <doi:10.1177/0962280219889080> and Cai et al. (2021) 
    <doi:10.1177/09622802211047348> for estimating the sample mean and standard 
    deviation from commonly reported quantiles in meta-analysis. These methods 
    can be applied to studies that report the sample median, sample size, and 
    one or both of (i) the sample minimum and maximum values and (ii) the first 
    and third quartiles. The corresponding standard error estimators described 
    by McGrath et al. (2023) <doi:10.1177/09622802221139233> are also included.
	"""
	
	homepage = "https://github.com/stmcg/estmeansd"
	cran = "estmeansd" 

	version("1.0.1", md5="5dd35853ecf07a83133b7d8755c3eca9")

	depends_on("r-metablue", type=("build", "run"))
