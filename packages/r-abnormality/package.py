# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbnormality(RPackage):
	"""Measure a Subject's Abnormality with Respect to a Reference
Population

	Contains the functions to implement the methodology and considerations laid out by Marks et al. in the manuscript Measuring Abnormality in High Dimensional Spaces: Applications in Biomechanical Gait Analysis. As of 2/27/2018 this paper has been submitted and is under scientific review. Using high-dimensional datasets to measure a subject’s overall level of abnormality as compared to a reference population is often needed in outcomes research. Utilizing applications in instrumented gait analysis, that article demonstrates how using data that is inherently non-independent to measure overall abnormality may bias results. A methodology is introduced to address this bias to accurately measure overall abnormality in high dimensional spaces. While this methodology is in line with previous literature, it differs in two major ways. Advantageously, it can be applied to datasets in which the number of observations is less than the number of features/variables, and it can be abstracted to practically any number of domains or dimensions. After applying the proposed methodology to the original data, the researcher is left with a set of uncorrelated variables (i.e. principal components) with which overall abnormality can be measured without bias. Different considerations are discussed in that article in deciding the appropriate number of principal components to keep and the aggregate distance measure to utilize.
	"""
	
	cran = "abnormality" 

	version("0.1.0", md5="da052e7d38d02c5c050e7879f2713345")

	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
