# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpr(RPackage):
	"""Iterative Proportional Repartition Algorithm

	Let us consider a sample of patients who can suffer from several diseases simultaneously, in a given set of diseases. The goal of the implemented algorithm is to estimate the individual average cost of each disease, starting from the global health costs available for each patient.
	"""
	
	cran = "ipr" 

	version("0.1.0", md5="803877e29693611ffbedf956f7f6f555")

