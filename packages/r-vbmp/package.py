# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVbmp(RPackage):
	"""Variational Bayesian Multinomial Probit Regression

	Variational Bayesian Multinomial Probit Regression with Gaussian Process Priors. It estimates class membership posterior probability employing variational and sparse approximation to the full posterior. This software also incorporates feature weighting by means of Automatic Relevance Determination.
	"""
	
	homepage = "http://bioinformatics.oxfordjournals.org/cgi/content/short/btm535v1"
	bioc = "vbmp" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/vbmp_1.70.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/vbmp/vbmp_1.70.0.tar.gz"]

	version("1.70.0", md5="b7d2a0a9950dd7ecdbcea5ffdfbd853c")

	depends_on("r@2.10:", type=("build", "run"))
