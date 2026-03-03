# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmitidstruct(RPackage):
	"""Data Structure and Manipulations Tool for Host and Viral
Population

	Statistical Methods for Inferring Transmissions of Infectious Diseases from deep sequencing data (SMITID).
  It allow sequence-space-time host and viral population data storage, indexation and querying.
	"""
	
	homepage = "https://informatique-mia.inra.fr/biosp/anr-smitid-project"
	cran = "SMITIDstruct" 

	version("0.0.5", md5="6eab4948f9f0e34c061f4ba262f51173")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sf@0.6.3:", type=("build", "run"))
	depends_on("r-biostrings@2:", type=("build", "run"))
