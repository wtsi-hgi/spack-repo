# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXlink(RPackage):
	"""Genetic Association Models for X-Chromosome SNPS on Continuous,
Binary and Survival Outcomes

	The expression of X-chromosome undergoes three possible biological processes: X-chromosome
             inactivation (XCI), escape of the X-chromosome inactivation (XCI-E),and skewed X-chromosome                    
             inactivation (XCI-S). To analyze the X-linked genetic association for phenotype such as                         
             continuous, binary, and time-to-event outcomes with the actual process unknown, we propose a unified            
             approach of maximizing the likelihood or partial likelihood over all of the potential biological             
             processes. The methods are described in Wei Xu, Meiling Hao (2017) <doi:10.1002/gepi.22097>. And 
             also see Dongxiao Han, Meiling Hao, Lianqiang Qu, Wei Xu (2019) <doi:10.1177/0962280219859037>.
	"""
	
	homepage = "https://github.com/qiuanzhu/xlink"
	cran = "xlink" 

	version("1.0.1", md5="44860cfe9345a8dc20f3c31c6bde3fa8")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-survival@2.41.3:", type=("build", "run"))
