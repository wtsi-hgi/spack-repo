# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgsda(RPackage):
	"""Multi-Group Sparse Discriminant Analysis

	Implements Multi-Group Sparse Discriminant Analysis proposal of I.Gaynanova, J.Booth and M.Wells (2016), Simultaneous sparse estimation of canonical vectors in the p>>N setting, JASA <doi:10.1080/01621459.2015.1034318>.
	"""
	
	cran = "MGSDA" 

	version("1.6.1", md5="e1bcc9c6d006a755c42714b87f0a1802")

	depends_on("r-mass", type=("build", "run"))
