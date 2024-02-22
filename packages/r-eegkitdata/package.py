# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REegkitdata(RPackage):
	"""Electroencephalography Toolkit Datasets

	Contains the example EEG data used in the package eegkit. Also contains code for easily creating larger EEG datasets from the EEG Database on the UCI Machine Learning Repository.
	"""
	
	cran = "eegkitdata" 

	version("1.1", md5="56930af150cc41dcb8157358ed21b0f8")

	depends_on("r@2.10:", type=("build", "run"))
