# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAccsda(RPackage):
	"""Accelerated Sparse Discriminant Analysis

	Implementation of sparse linear discriminant analysis, which is a supervised
    classification method for multiple classes. Various novel optimization approaches to
    this problem are implemented including alternating direction method of multipliers ('ADMM'),
    proximal gradient (PG) and accelerated proximal gradient ('APG') (See Atkins 'et al'. <arXiv:1705.07194>).
    Functions for performing cross validation are also supplied along with basic prediction
    and plotting functions.
    Sparse zero variance discriminant analysis ('SZVD') is also included in the package
    (See Ames and Hong, <arXiv:1401.5492>). See the 'github' wiki for a more extended description.
	"""
	
	homepage = "https://github.com/gumeo/accSDA/wiki"
	cran = "accSDA" 

	version("1.1.3", md5="f69de7acb8a6fbfb5204b4964704491b")
	version("1.1.2", md5="7f357940ffdb072548b642ba605dac16")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mass@7.3.45:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-gridextra@2.2.1:", type=("build", "run"))
