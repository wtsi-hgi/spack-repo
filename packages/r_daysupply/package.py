# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaysupply(RPackage):
	"""Calculating Days' Supply and Daily Dose of Prescriptions

	Allows clinicians and researchers to compute daily dose (and subsequently days' supply) for prescription refills using the following methods: Fixed window, fixed tablet, defined daily dose (DDD), and Random Effects Warfarin Days' Supply (REWarDS). Daily dose is the computed dose that the patient takes every day. For medications with fixed dosing (e.g. direct oral anticoagulants) this is known and does not need to be estimated. For medications with varying dose such as warfarin, however, the daily dose should be assumed or estimated to allow measurement of drug exposure. Days’ supply is the number of days that patients’ supply of medication will last after each prescription fill. Estimating days’ supply is necessary to calculate drug exposure. The package computes days’ supply and daily dose at both the prescription and patient levels. Results at the prescription level are denoted with “-Rx-” and those at patient level are denoted with “-Pt-”.
	"""
	
	cran = "daySupply" 

	version("0.1.0", md5="234b37cd3a7cf4c2c3992140bb82136f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
