# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQcewas(RPackage):
	"""Fast and Easy Quality Control of EWAS Results Files

	Tools for (automated and manual) quality control of 
  the results of Epigenome-Wide Association Studies.
	"""
	
	cran = "QCEWAS" 

	version("1.2-3", md5="caa40ed34a76c3825cb3a145a29c7c52")

	depends_on("r@4:", type=("build", "run"))
