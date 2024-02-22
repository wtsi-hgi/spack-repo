# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdcorsv(RPackage):
	"""Linkage Disequilibrium Corrected by the Structure and the
Relatedness

	Four measures of linkage disequilibrium are provided: the usual r^2
        measure, the r^2_S measure (r^2 corrected by the structure
        sample), the r^2_V (r^2 corrected by the relatedness of
        genotyped individuals), the r^2_VS measure (r^2 corrected by
        both the relatedness of genotyped individuals and the structure
        of the sample).
	"""
	
	cran = "LDcorSV" 

	version("1.3.3", md5="4f7d7bb91071c0d8b5166fca2f56aeed")

