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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/proteinProfiles_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/proteinProfiles/proteinProfiles_1.42.0.tar.gz"]

	version("1.42.0", sha256="81a9c27835eddd7c31155031dc19488487f3ca869ad07e069407ff4b6ada5694")

	depends_on("r@2.15.2:", type=("build", "run"))
