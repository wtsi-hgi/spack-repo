# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProstatecancertaylor(RPackage):
	"""Prostate Cancer Data

	A Bioconductor data package for the Taylor et al (2010) dataset.
	"""
	
	bioc = "prostateCancerTaylor" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/prostateCancerTaylor_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/prostateCancerTaylor/prostateCancerTaylor_1.30.0.tar.gz"]

	version("1.30.0", sha256="7c0afc3b5055dcab296f6c730feb59ef2a6bb3fe91592f2f955ed9ccdd608c55")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r@3.3:", type=("build", "run"))

