# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowerindexr(RPackage):
	"""Measuring the Power in Voting Systems

	This R package allows the determination of some distributions of 
             the voters' power when passing laws in weighted voting situations.
	"""
	
	cran = "powerindexR" 

	version("1.5", md5="9d158143dc38c38f127c927e858c98b4")

	depends_on("r@3:", type=("build", "run"))
