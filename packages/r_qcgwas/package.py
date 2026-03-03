# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQcgwas(RPackage):
	"""Quality Control of Genome Wide Association Study Results

	Tools for (automated and manual) quality control of the results of Genome Wide Association Studies.
	"""
	
	cran = "QCGWAS" 

	version("1.0-9", md5="30ba6356e7892a8e292d4f20cb94fad6")

	depends_on("r@4:", type=("build", "run"))
