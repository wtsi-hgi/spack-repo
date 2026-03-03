# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnlinebcp(RPackage):
	"""Online Bayesian Methods for Change Point Analysis

	It implements the online Bayesian methods for change point analysis. It can
            also perform missing data imputation with methods from 'VIM'. The reference 
            is Yigiter A, Chen J, An L, Danacioglu N (2015) <doi:10.1080/02664763.2014.1001330>. 
            The link to the package is <https://CRAN.R-project.org/package=onlineBcp>.
	"""
	
	cran = "onlineBcp" 

	version("0.1.8", md5="28373aa55f7edd401577f5b393d275ec")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-vim", type=("build", "run"))
