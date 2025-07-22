# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcaspar(RPackage):
	"""A package for survival time prediction based on a piecewise baseline hazard Cox regression model.

	The package is the R-version of the C-based software bold{CASPAR} (Kaderali,2006: url{http://bioinformatics.oxfordjournals.org/content/22/12/1495}). It is meant to help predict survival times in the presence of high-dimensional explanatory covariates. The model is a piecewise baseline hazard Cox regression model with an Lq-norm based prior that selects for the most important regression coefficients, and in turn the most relevant covariates for survival analysis. It was primarily tried on gene expression and aCGH data, but can be used on any other type of high-dimensional data and in disciplines other than biology and medicine.
	"""
	
	bioc = "RCASPAR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RCASPAR_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RCASPAR/RCASPAR_1.48.0.tar.gz"]

	version("1.54.0", tag="RELEASE_3_21")
	version("1.48.0", sha256="07a6ffe4517664205847a8161ed0b8ccdbdfafd384ee0961688d1ec4540ce102")

