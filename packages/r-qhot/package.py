# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQhot(RPackage):
	"""QTL Hotspot Detection

	This function produces both the numerical and graphical summaries of the QTL hotspot detection in the genomes that are available on the worldwide web including the flanking markers of QTLs.
	"""
	
	cran = "QHOT" 

	version("0.1.0", md5="11e78be7925506de993b2213d8d400a0")

