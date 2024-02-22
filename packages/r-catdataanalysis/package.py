# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatdataanalysis(RPackage):
	"""Datasets for Categorical Data Analysis by Agresti

	Datasets used in the book "Categorical Data Analysis"
   by Agresti (2012, ISBN:978-0-470-46363-5) but not printed in the book.
   Datasets and help pages were automatically produced from the source
   <https://users.stat.ufl.edu/~aa/cda/data.html> by the R script foo.R,
   which can be found in the GitHub repository.
	"""
	
	homepage = "https://github.com/cjgeyer/CatDataAnalysis"
	cran = "CatDataAnalysis" 

	version("0.1-5", md5="c089fefaab82e9156369145526514710")

	depends_on("r@3.0.2:", type=("build", "run"))
