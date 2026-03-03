# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNecklaces(RPackage):
	"""Necklaces and Bracelets

	Tools to generate Necklaces, Bracelets, Lyndon words and de Bruijn sequences. The generation relies on integer partitions and uses the 'KStatistics' package. Methods used in the package refers to E. Di Nardo and G. Guarino (2022) <arXiv:2208.06855>. 
	"""
	
	cran = "Necklaces" 

	version("1.0", md5="bcc01517ef0f19e42b6fadedaa8a1392")

	depends_on("r-kstatistics", type=("build", "run"))
