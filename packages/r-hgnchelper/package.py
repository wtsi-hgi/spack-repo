# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgnchelper(RPackage):
	"""Identify and Correct Invalid HGNC Human Gene Symbols and MGI
Mouse Gene Symbols

	Contains functions for
 identifying and correcting HGNC human gene symbols and MGI mouse gene symbols 
 which have been converted to date format by Excel, withdrawn, or aliased.
 Also contains functions for reversibly converting between HGNC
 symbols and valid R names.
	"""
	
	homepage = "https://github.com/waldronlab/HGNChelper"
	cran = "HGNChelper" 

	version("0.8.1", md5="45d4542ac3250350b96c3c9506acffcc")

	depends_on("r@3.5:", type=("build", "run"))
