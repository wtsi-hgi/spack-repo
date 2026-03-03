# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROuterbase(RPackage):
	"""Outer Product Regression

	High-dimensional regression using outer product models.  Research on the methods is currently under investigation and published resources will be posted as they are available.  As the method is new, the website is the best resource for understanding the principals. Some of the core ideas are based on Plumlee and coauthors' work on analysis of grid-structured  experiments described in Plumlee (2014) <doi:10.1080/01621459.2014.900250> and  Plumlee, Erickson, Ankenman, Lawrence (2021) <doi:10.1093/biomet/asaa084>.  Some additional textbooks for additional information on Gaussian processes are Rasmussen and Williams (2005) <doi:10.7551/mitpress/3206.001.0001> and  Gramacy (2022) <doi:10.1201/9780367815493>.
	"""
	
	homepage = "https://mattplumlee.github.io/outerbase/"
	cran = "outerbase" 

	version("0.1.0", md5="dbe3af4defcc1949ce933d8b78b845e6")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
