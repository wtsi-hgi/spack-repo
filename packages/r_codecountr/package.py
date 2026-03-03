# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodecountr(RPackage):
	"""Counting Codes in a Text and Preparing Data for Analysis

	Data analysis frequently requires coding, in particular when data are collected by interviews, by observations or even by questionnaires. Therefore, code counting and data preparation are necessary phases to carry out the analysis. Thus, the analysts will wish to count the codes inserted in a text (tokenization and counting of a list of pre-established codes) and to carry out the preparation of the data (feature scaling min-max normalization, Zscore, Box and Cox transformation, non parametric bootstrap). For Box and Cox (1964) <https://www.jstor.org/stable/2984418> transformation, optimal Lambda is calculated by log-likelihood. Non parametric bootstrap is based on randomly sampling data with replacement. Package for educational purposes. 
	"""
	
	cran = "codecountR" 

	version("0.0.4.0", md5="e4bbf89a9f8eb44fe04e5b7e328d8cd8")

