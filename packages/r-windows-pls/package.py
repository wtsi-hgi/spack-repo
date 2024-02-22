# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWindowsPls(RPackage):
	"""Segmentation Approaches in Chemometrics

	Evaluation of prediction performance of smaller regions of
    spectra for Chemometrics. Segmentation of spectra, evolving dimensions
    regions and sliding windows as selection methods. Election of the best
    model among those computed based on error metrics. Chen et al.(2017)
    <doi:10.1007/s00216-017-0218-9>.
	"""
	
	homepage = "https://github.com/egonzato/windows.pls"
	cran = "windows.pls" 

	version("0.1.0", md5="6cfb93cdabbc4ae571a94d95f9cf83c1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mdatools", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
