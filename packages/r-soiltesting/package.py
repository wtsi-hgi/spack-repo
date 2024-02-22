# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoiltesting(RPackage):
	"""Organic Carbon and Plant Available Nutrient Contents in Soil

	Testing of soil for the contents of organic carbon, and available macro- and micro-nutrients is a crucial part of soil fertility assessment. This package computes some routinely tested soil properties viz. organic carbon (C), total nitrogen (N), available N, mineral N, available phosphorus (P), available potassium (K), available iron (Fe), available zinc (Zn), available manganese (Mn), available copper (Cu), and available nickel (Ni) in soil based on laboratory analysis data obtained by most commonly followed protocols. Besides, it can also draw standard curves based on absorption/emission vs. concentration data, and give out unknown concentrations from absorption/emission readings.
	"""
	
	cran = "SoilTesting" 

	version("0.1.0", md5="3b838ef9adccec6e421bf57a7beea20b")

