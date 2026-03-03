# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDescr(RPackage):
	"""Descriptive Statistics

	Weighted frequency and contingency tables of categorical
       variables and of the comparison of the mean value of a numerical
       variable by the levels of a factor, and methods to produce xtable
       objects of the tables and to plot them. There are also functions to
       facilitate the character encoding conversion of objects, to quickly
       convert fixed width files into csv ones, and to export a data.frame to
       a text file with the necessary R and SPSS codes to reread the data.
	"""
	
	homepage = "https://github.com/jalvesaq/descr"
	cran = "descr" 

	version("1.1.8", md5="165e2705bbe8c4b8312dae83f385990f")

	depends_on("r-xtable", type=("build", "run"))
