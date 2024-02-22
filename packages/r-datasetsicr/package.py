# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatasetsicr(RPackage):
	"""Datasets from the Book "An Introduction to Clustering with R"

	Companion to the book "An Introduction to Clustering with R" by P. Giordani, M.B. Ferraro and F. Martella (Springer, Singapore, 2020). The datasets are used in some case studies throughout the text.
	"""
	
	cran = "datasetsICR" 

	version("1.0", md5="23cd02d637f2c0e491a8fa0592870fb3")

	depends_on("r@3.5:", type=("build", "run"))
