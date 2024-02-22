# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArchaeophasesDataset(RPackage):
	"""Data Sets for 'ArchaeoPhases' Vignettes

	Provides the data sets used to build the 'ArchaeoPhases' vignettes.  The data sets were formerly distributed with 'ArchaeoPhases', however they exceed current CRAN policy for package size.
	"""
	
	cran = "ArchaeoPhases.dataset" 

	version("0.2.0", md5="186b679c7a4d44ce9ef36f4a1bdbb820")

	depends_on("r@3.5:", type=("build", "run"))
