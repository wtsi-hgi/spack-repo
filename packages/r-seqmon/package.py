# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqmon(RPackage):
	"""Group Sequential Design Class for Clinical Trials

	S4 class object for creating and managing group sequential designs. It calculates the efficacy and futility boundaries at each look. It allows modifying the design and tracking the design update history.
	"""
	
	cran = "seqmon" 

	version("2.4", md5="7894ccb88e12f75fd0abc748925b55f4")

