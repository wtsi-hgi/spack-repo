# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSupportBws2(RPackage):
	"""Tools for Case 2 Best-Worst Scaling

	Provides three basic functions that support an implementation of Case 2 (profile case) best-worst scaling. The first is to convert an orthogonal main-effect design into questions, the second is to create a dataset suitable for analysis, and the third is to calculate count-based scores. For details, see Aizaki and Fogarty (2019) <doi:10.1016/j.jocm.2019.100171>.
	"""
	
	cran = "support.BWS2" 

	version("0.4-0", md5="f38ebb902bc5cbb304d095d374be5b87", url="https://cran.r-project.org/src/contrib/support.BWS2_0.4-0.tar.gz")

