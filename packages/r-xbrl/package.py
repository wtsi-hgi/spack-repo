# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXbrl(RPackage):
	"""Extraction of Business Financial Information from 'XBRL'
Documents

	
  Functions to extract business financial information from
  an Extensible Business Reporting Language ('XBRL') instance file and the
  associated collection of files that defines its 'Discoverable' Taxonomy
  Set ('DTS').
	"""
	
	cran = "XBRL" 

	version("0.99.19.1", md5="58452df50e1ac4325b9ee67eb37fdc38")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("libxml2@2.9.1:", type=("build", "link", "run"))
