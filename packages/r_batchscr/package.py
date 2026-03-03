# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBatchscr(RPackage):
	"""Batch Script Helpers

	Handy frameworks, such as error handling and log generation, for batch scripts.
	Use case: in scripts running in remote servers, set error handling mechanism for downloading and uploading and record operation log.
	"""
	
	cran = "batchscr" 

	version("0.1.0", md5="dca74e130eb8826f01ea5bf94c0387d6")

