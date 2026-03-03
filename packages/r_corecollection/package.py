# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorecollection(RPackage):
	"""Core Collection

	
  Create a custom sized Core Collection based on a distance matrix and applying
  the A-NE (accession nearest entry), E-NE (entry nearest entry) or E-E (entry entry) method
  as introduced in Jansen and van Hintum (2007) <doi:10.1007/s00122-006-0433-9> and
  further elaborated on in Odong, T.L. (2012) <https://edepot.wur.nl/212422>.
  Optionally a list of preselected accessions to be included into the core can be set.
  For each accession in the computed core, if available nearby accessions are retrievable
  that can be used as an alternative.
	"""
	
	cran = "coreCollection" 

	version("0.9.5", md5="b7ea07aa459835f11952a41a84770e22")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6@2.4:", type=("build", "run"))
