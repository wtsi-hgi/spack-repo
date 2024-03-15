# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeguid(RPackage):
	"""Sequence Globally Unique Identifier (SEGUID) Checksums

	Implementation of the original Sequence Globally Unique Identifier (SEGUID) algorithm [Babnigg and Giometti (2006) <doi:10.1002/pmic.200600032>] and SEGUID v2 (<https://www.seguid.org>), which extends SEGUID v1 with support for linear, circular, single- and double-stranded biological sequences, e.g. DNA, RNA, and proteins.
	"""
	
	homepage = "https://www.seguid.org/"
	cran = "seguid" 

	version("0.1.0", md5="78a101394f7c7f7f01a6c7579f9e2a6f")

	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
