# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHrw(RPackage):
	"""Datasets, Functions and Scripts for Semiparametric Regression
Supporting Harezlak, Ruppert & Wand (2018)

	The book "Semiparametric Regression with R" by J. Harezlak, D. Ruppert & M.P. Wand (2018, Springer; ISBN: 978-1-4939-8851-8) makes use of datasets and scripts to explain semiparametric regression concepts. Each of the book's scripts are contained in this package as well as datasets that are not within other R packages. Functions that aid semiparametric regression analysis are also included.
	"""
	
	cran = "HRW" 

	version("1.0-5", md5="b575c9d4f535d103cbd1ffdd38828b4c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
