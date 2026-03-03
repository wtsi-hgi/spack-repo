# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCleanbsequences(RPackage):
	"""Curing of Biological Sequences

	Curates biological sequences massively, quickly, without errors and 
 without internet connection.  Biological sequences curing is performed by 
 aligning the forward and / or revers primers or ends of cloning vectors with the sequences 
 to be cleaned. After the alignment, new subsequences are generated without biological fragment 
 not desired by the user.
 Pozzi et al (2020) <doi:10.1007/s00438-020-01671-z>.
	"""
	
	cran = "CleanBSequences" 

	version("1.4.0", md5="4b53fefc2c4ae310a0ed7dd9369dac50")

	depends_on("r-biostrings", type=("build", "run"))
