# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJcrimpactfactor(RPackage):
	"""Journal Citation Reports ('JCR') Impact Factor by 'Clarivate'
'Analytics'

	The Impact Factor of a journal reported by Journal Citation Reports ('JCR') of  'Clarivate' 'Analytics' is provided. The impact factor is available for those journals only that were included Journal Citation Reports 'JCR'.
	"""
	
	cran = "JCRImpactFactor" 

	version("1.0.0", md5="9d6fe55b0ca488b42704486408d5f4a4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
