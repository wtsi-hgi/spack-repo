# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalculatorLrFns(RPackage):
	"""Calculator for LR Fuzzy Numbers

	Arithmetic operations scalar multiplication, addition, subtraction, multiplication and division of LR fuzzy numbers (which are on the basis of extension principle) have a complicate form for using in fuzzy Statistics, fuzzy Mathematics, machine learning, fuzzy data analysis and etc. Calculator for LR Fuzzy Numbers package relieve and aid applied users to achieve a simple and closed form for some complicated operator based on LR fuzzy numbers and also the user can easily draw the membership function of the obtained result by this package. 
	"""
	
	cran = "Calculator.LR.FNs" 

	version("1.3", md5="76bab99c3c70162029437a7c84a741ef")

