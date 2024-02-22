# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTergm(RPackage):
	"""Fit, Simulate and Diagnose Models for Network Evolution Based on
Exponential-Family Random Graph Models

	An integrated set of extensions to the 'ergm' package to analyze and simulate network evolution based on exponential-family random graph models (ERGM). 'tergm' is a part of the 'statnet' suite of packages for network analysis. See Krivitsky and Handcock (2014) <doi:10.1111/rssb.12014> and Carnegie, Krivitsky, Hunter, and Goodreau (2015) <doi:10.1080/10618600.2014.903087>.
	"""
	
	homepage = "https://statnet.org"
	cran = "tergm" 

	version("4.2.0", md5="0a5aa26cb17781a91e487eff44948102")

	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-network@1.18:", type=("build", "run"))
	depends_on("r-networkdynamic@0.11.3:", type=("build", "run"))
	depends_on("r-robustbase@0.93.5:", type=("build", "run"))
	depends_on("r-coda@0.19.2:", type=("build", "run"))
	depends_on("r-nlme@3.1.139:", type=("build", "run"))
	depends_on("r-mass@7.3.51.4:", type=("build", "run"))
	depends_on("r-statnet-common@4.9:", type=("build", "run"))
	depends_on("r-ergm-multi@0.2:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
