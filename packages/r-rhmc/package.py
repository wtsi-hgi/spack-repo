# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhmc(RPackage):
	"""Hamiltonian Monte Carlo

	Implements simple Hamiltonian Monte Carlo routines in R for
             sampling from any desired target distribution which is continuous
             and smooth. See Neal (2017) <arXiv:1701.02434> for further details
             on Hamiltonian Monte Carlo. Automatic parameter selection is not
             supported.
	"""
	
	cran = "rhmc" 

	version("1.0.0", md5="a71c47038a57c34333ed19cdb94652cf")

