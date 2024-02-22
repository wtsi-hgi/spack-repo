# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProteinprofiles(RPackage):
	"""Protein Profiling

	Significance assessment for distance measures of time-course protein profiles
	"""
	
	bioc = "proteinProfiles" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/proteinProfiles_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/proteinProfiles/proteinProfiles_1.42.0.tar.gz"]

	version("1.42.0", md5="491483ff7b360413ae0eafa5ac07de14")

	depends_on("r@2.15.2:", type=("build", "run"))
