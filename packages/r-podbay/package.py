# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPodbay(RPackage):
	"""Vaccine Efficacy Estimation Package

	Set of functions that implement the PoDBAY method, described in the publication 'A method to estimate probability of disease and vaccine efficacy from clinical trial immunogenicity data' by Julie Dudasova, Regina Laube, Chandni Valiathan, Matthew C. Wiener, Ferdous Gheyas, Pavel Fiser, Justina Ivanauskaite, Frank Liu and Jeffrey R. Sachs (NPJ Vaccines, 2021), <doi:10.1038/s41541-021-00377-6>.
	"""
	
	cran = "PoDBAY" 

	version("1.4.3", md5="f650af55b278eaed0fcf7ee1f714d012")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
