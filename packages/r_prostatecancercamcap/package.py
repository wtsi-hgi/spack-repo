# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProstatecancercamcap(RPackage):
	"""Prostate Cancer Data

	A Bioconductor data package for the Ross-Adams (2015) Prostate Cancer dataset.
	"""
	
	bioc = "prostateCancerCamcap" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/prostateCancerCamcap_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/prostateCancerCamcap/prostateCancerCamcap_1.30.0.tar.gz"]

	version("1.30.0", md5="5a27ee47f07162569e5e1e06ffd69886")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r@3.3:", type=("build", "run"))

