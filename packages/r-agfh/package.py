# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgfh(RPackage):
	"""Agnostic Fay-Herriot Model for Small Area Statistics

	Implements the Agnostic Fay-Herriot model, an extension of 
    the traditional small area model. In place of normal sampling errors, the 
    sampling error distribution is estimated with a Gaussian process to 
    accommodate a broader class of distributions. This flexibility is most 
    useful in the presence of bounded, multi-modal, or heavily skewed sampling 
    errors.
	"""
	
	cran = "agfh" 

	version("0.2.1", md5="290b6ca3fd011c8f293900eee10282d8")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-goftest", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
