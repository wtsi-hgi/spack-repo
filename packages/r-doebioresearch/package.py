# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoebioresearch(RPackage):
	"""Analysis of Design of Experiments for Biological Research

	Performs analysis of popular experimental designs used in the field of biological research. The designs covered are completely randomized design, randomized complete block design, factorial completely randomized design, factorial randomized complete block design, split plot design, strip plot design and latin square design. The analysis include analysis of variance, coefficient of determination, normality test of residuals, standard error of mean, standard error of difference and multiple comparison test of means. The package has functions for transformation of data and yield data conversion. Some datasets are also added in order to facilitate examples.
	"""
	
	cran = "doebioresearch" 

	version("0.1.0", md5="07774e37b8a405d3916f8887b9facee1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-agricolae@1.3.3:", type=("build", "run"))
