# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeddietcalc(RPackage):
	"""Multi Calculator to Compute Scores of Adherence to Mediterranean
Diet

	Multi Calculator of different scores to measure adherence to Mediterranean Diet, to compute them in nutriepidemiological data. Additionally, a sample dataset of this kind of data is provided, and some other minor tools useful in epidemiological studies.
	"""
	
	cran = "MedDietCalc" 

	version("0.1.1", md5="d4875d5863b078ab753dee74df1377ca")

