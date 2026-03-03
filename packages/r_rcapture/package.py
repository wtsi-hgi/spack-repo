# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcapture(RPackage):
	"""Loglinear Models for Capture-Recapture Experiments

	Estimation of abundance and other demographic parameters for closed 
             populations, open populations and the robust design in capture-recapture  
             experiments using loglinear models.   
	"""
	
	cran = "Rcapture" 

	version("1.4-4", md5="2f1d98af31f28b054c0ab61cd7320c86")

