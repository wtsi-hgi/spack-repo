# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCepreader(RPackage):
	"""Read 'CEP' and Legacy 'CANOCO' Files

	Read Condensed Cornell Ecology Program ('CEP') and legacy
    'CANOCO' files into R data frames.
	"""
	
	homepage = "https://cran.r-project.org/"
	cran = "cepreader" 

	version("1.2-2", md5="6c59a84ceb7508e96907a4436e4ac696")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
