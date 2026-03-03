# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStratification(RPackage):
	"""Univariate Stratification of Survey Populations

	Univariate stratification of survey populations with a generalization of the 
  Lavallee-Hidiroglou method of stratum construction. The generalized method takes into account 
  a discrepancy between the stratification variable and the survey variable. The determination 
  of the optimal boundaries also incorporate, if desired, an anticipated non-response, a take-all 
  stratum for large units, a take-none stratum for small units, and a certainty stratum to ensure 
  that some specific units are in the sample. The well known cumulative root frequency rule of 
  Dalenius and Hodges and the geometric rule of Gunning and Horgan are also implemented. 
	"""
	
	cran = "stratification" 

	version("2.2-7", md5="a648b5359c4d7f29b01e92a973f2a16b")

