# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProstatecancervarambally(RPackage):
	"""Prostate Cancer Data

	A Bioconductor data package for the Varambally dataset
	"""
	
	bioc = "prostateCancerVarambally" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/prostateCancerVarambally_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/prostateCancerVarambally/prostateCancerVarambally_1.30.0.tar.gz"]

	version("1.30.0", md5="cf8fc1872af8c5c2b47372ce94ed4c5c")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r@3.3:", type=("build", "run"))

	# experiment