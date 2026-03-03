# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbddirichlet(RPackage):
	"""NBD-Dirichlet Model of Consumer Buying Behavior for Marketing
Research

	The Dirichlet (aka NBD-Dirichlet) model describes the purchase incidence and brand choice of consumer products.  We estimate the model and summarize various theoretical quantities of interest to marketing researchers. Also provides functions for making tables that compare observed and theoretical statistics. 
	"""
	
	homepage = "https://ani.stat.fsu.edu/~fchen/statistics/R-package-NBDdirichlet/how-to-use-Dirichlet-marketing-model.html"
	cran = "NBDdirichlet" 

	version("1.4", md5="388e4e4786faf6432e8b76b05c9dfb75")

