# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmicsqc(RPackage):
	"""Nominating Quality Control Outliers in Genomic Profiling Studies

	A method that analyzes quality control metrics from multi-sample genomic sequencing studies and nominates poor quality samples for exclusion. Per sample quality control data are transformed into z-scores and aggregated. The distribution of aggregated z-scores are modelled using parametric distributions. The parameters of the optimal model, selected either by goodness-of-fit statistics or user-designation, are used for outlier nomination. Two implementations of the Cosine Similarity Outlier Detection algorithm are provided with flexible parameters for dataset customization.
	"""
	
	cran = "OmicsQC" 

	version("1.1.0", md5="fa80b01428f54f0563b12dff44dea8c9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-lsa", type=("build", "run"))
	depends_on("r-boutroslab-plotting-general", type=("build", "run"))
