# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWyzCodeMetatesting(RPackage):
	"""Wizardry Code Meta Testing

	Meta testing is the ability to test a function without having to 
    provide its parameter values.
    Those values will be generated, based on semantic naming of parameters, as 
    introduced by package 'wyz.code.offensiveProgramming'.
    Value generation logic can be completed with your own data types 
    and generation schemes. This to meet your most specific requirements and to 
    answer to a wide variety of usages, from general use case to very specific
    ones.
    While using meta testing, it becomes easier to generate stress test 
    campaigns, non-regression test campaigns and robustness test campaigns, as 
    generated tests can be saved and reused from session to session. 
    Main benefits of using 'wyz.code.metaTesting' is ability to discover valid 
    and invalid function parameter combinations, ability to infer valid 
    parameter values, and to provide smart summaries that allows you to focus
    on dysfunctional cases. 
	"""
	
	homepage = "https://neonira.github.io/offensiveProgrammingBook_v1.2.2/"
	cran = "wyz.code.metaTesting" 

	version("1.1.22", md5="97d874e7429740ed22105d3ca7503015")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table@1.11.8:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-wyz-code-offensiveprogramming@1.1.22:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
