# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaboqc(RPackage):
	"""Normalize Metabolomic Data using QC Signal

	Takes QC signal for each day and normalize metabolomic
    data that has been acquired in a certain period of time. At least
    three QC per day are required.
	"""
	
	cran = "MetaboQC" 

	version("1.1", md5="08e1239952f40897e2681ff7e5be4092")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
