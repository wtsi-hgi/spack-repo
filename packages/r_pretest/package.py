# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPretest(RPackage):
	"""A Novel Approach to Predictive Accuracy Testing in Nested
Environments

	This repository contains the codes for using the predictive accuracy comparison tests developed in Pitarakis, J. (2023) <doi:10.1017/S0266466623000154>. 
	"""
	
	cran = "pretest" 

	version("0.2", md5="aa46904d7e89385cd1db1ef45121e638")

