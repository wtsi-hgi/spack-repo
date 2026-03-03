# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsia(RPackage):
	"""Import and Analysis of OMR Data from FormScanner

	Import data of tests and questionnaires from FormScanner. FormScanner is an open source software that converts scanned images to data using optical mark recognition (OMR) and it can be downloaded from <http://sourceforge.net/projects/formscanner/>. The spreadsheet file created by FormScanner is imported in a convenient format to perform the analyses provided by the package. These analyses include the conversion of multiple responses to binary (correct/incorrect) data, the computation of the number of corrected responses for each subject or item, scoring using weights,the computation and the graphical representation of the frequencies of the responses to each item and the report of the responses of a few subjects.
	"""
	
	cran = "fsia" 

	version("1.1.1", md5="d8def48ae54dc31790d0db6392c29f68")

