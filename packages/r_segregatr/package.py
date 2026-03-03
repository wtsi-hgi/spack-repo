# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSegregatr(RPackage):
	"""Segregation Analysis for Variant Interpretation

	An implementation of the full-likelihood Bayes factor (FLB) 
    for evaluating segregation evidence in clinical medical genetics. The method 
    was introduced by Thompson et al. (2003) <doi:10.1086/378100>, and further 
    popularised by Bayrak-Toydemir et al. (2008) <doi:10.1016/j.yexmp.2008.03.006>.
    This implementation allows custom penetrance values and liability classes, and 
    includes specialised pedigree visualisations.
	"""
	
	homepage = "https://github.com/magnusdv/segregatr"
	cran = "segregatr" 

	version("0.3.0", md5="bf1b96a5c75e3c6c5f29f3fc58681ace")

	depends_on("r-pedtools@2.2:", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-pedprobr", type=("build", "run"))
