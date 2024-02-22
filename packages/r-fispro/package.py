# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFispro(RPackage):
	"""Fuzzy Inference System Design and Optimization

	Fuzzy inference systems are based on fuzzy rules, which have a good capability for managing progressive phenomenons. 
  This package is a basic implementation of the main functions to use a Fuzzy Inference System (FIS) provided by the open source software 'FisPro' <https://www.fispro.org>. 
  'FisPro' allows to create fuzzy inference systems and to use them for reasoning purposes, especially for simulating a physical or biological system.
	"""
	
	homepage = "https://www.fispro.org"
	cran = "FisPro" 

	version("1.1.4", md5="38ac4d628f0dca3e048d5ad8a377111c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
