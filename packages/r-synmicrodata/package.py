# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynmicrodata(RPackage):
	"""Synthetic Microdata Generator

	This tool fits a non-parametric Bayesian model called "hierarchically
            coupled mixture model (HCMM)" to the original microdata in order to generate
            synthetic microdata for privacy protection. The non-parametric feature of the
            adopted model is useful for catching the joint distribution of the original data
            in a highly flexible manner, leading to the generation of synthetic data very
            similar to the original data. Important reference papers on this method include
            Murray & Reiter (2016) <doi:10.1080/01621459.2016.1174132>.
	"""
	
	cran = "synMicrodata" 

	version("1.0.0", md5="be751bdf7f924f8e689e5f4b86666fac")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
