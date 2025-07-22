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

    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="19373a600f351d97748530879bb856150ccf1083e52eedd30046f5a1afb37457")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r@3.3:", type=("build", "run"))

