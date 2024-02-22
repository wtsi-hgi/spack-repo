# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPearsonds(RPackage):
	"""Pearson Distribution System

	Implementation of the Pearson distribution system, including full
  support for the (d,p,q,r)-family of functions for probability distributions 
  and fitting via method of moments and maximum likelihood method.
	"""
	
	cran = "PearsonDS" 

	version("1.3.1", md5="afe9a4bf1ee2a5905806235296b50a03")

