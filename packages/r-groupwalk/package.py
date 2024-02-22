# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGroupwalk(RPackage):
	"""Implement the Group Walk Algorithm

	A procedure that uses target-decoy competition (or knockoffs) to reject multiple hypotheses in the presence of group structure. The procedure controls the false discovery rate (FDR) at a user-specified threshold.
	"""
	
	homepage = "https://www.biorxiv.org/content/10.1101/2022.01.30.478144v1"
	cran = "groupwalk" 

	version("0.1.2", md5="6fd158ea9c8213111b52822d4587e366")

