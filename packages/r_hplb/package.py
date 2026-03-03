# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHplb(RPackage):
	"""High-Probability Lower Bounds for the Total Variance Distance

	An implementation of high-probability lower bounds for the total variance distance 
             as introduced in Michel & Naef & Meinshausen (2020) <arXiv:2005.06006>. An estimated 
             lower-bound (with high-probability) on the total variation distance between two probability distributions from which
             samples are observed can be obtained with the function HPLB.
	"""
	
	cran = "HPLB" 

	version("1.0.0", md5="223472587b89363c0ac8b30682279666")

	depends_on("r-data-table", type=("build", "run"))
