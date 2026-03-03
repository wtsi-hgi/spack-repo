# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNaepprimer(RPackage):
	"""The NAEP Primer

	Contains a sample of the 2005 Grade 8 Mathematics data from the National Assessment of Educational Progress (NAEP). This data set is called the NAEP Primer.
	"""
	
	cran = "NAEPprimer" 

	version("1.0.1", md5="ec98467c103bed3f489180227908f2ee")

