# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBqtl(RPackage):
	"""Bayesian QTL Mapping Toolkit

	QTL mapping toolkit for inbred crosses and recombinant
        inbred lines. Includes maximum likelihood and Bayesian tools.
	"""
	
	cran = "bqtl" 

	version("1.0-36", md5="6d1851cc4934cd392d6139c126144a19")

	depends_on("r@2.6:", type=("build", "run"))
