# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProstatecancergrasso(RPackage):
	"""Prostate Cancer Data

	A Bioconductor data package for the Grasso (2012) Prostate Cancer dataset.
	"""
	
	bioc = "prostateCancerGrasso" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/prostateCancerGrasso_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/prostateCancerGrasso/prostateCancerGrasso_1.30.0.tar.gz"]

	version("1.30.0", md5="c331c996d943a14687439dfdf37b8029")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r@3.3:", type=("build", "run"))

	# experiment