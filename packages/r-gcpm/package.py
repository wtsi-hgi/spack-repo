# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcpm(RPackage):
	"""Generalized Credit Portfolio Model

	Analyze the default risk of credit portfolios. Commonly known models, 
		like CreditRisk+ or the CreditMetrics model are implemented in their very basic settings.
		The portfolio loss distribution can be achieved either by simulation or analytically 
		in case of the classic CreditRisk+ model. Models are only implemented to respect losses
		caused by defaults, i.e. migration risk is not included. The package structure is kept
		flexible especially with respect to distributional assumptions in order to quantify the
		sensitivity of risk figures with respect to several assumptions. Therefore the package
		can be used to determine the credit risk of a given portfolio as well as to quantify
		model sensitivities.
	"""
	
	cran = "GCPM" 

	version("1.2.2", md5="bd23d0f82089b844afb4e5be886ad9ed")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
