# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodbncbi(RPackage):
	"""biodbNcbi, a library for connecting to NCBI Databases.

	The biodbNcbi library provides access to the NCBI databases CCDS, Gene, Pubchem Comp and Pubchem Subst, using biodb package framework. It allows to retrieve entries by their accession number. Web services can be accessed for searching the database by name or mass.
	"""
	
	homepage = "https://github.com/pkrog/biodbNcbi"
	bioc = "biodbNcbi"

	version("1.12.0", commit="eff8ab9de075facaa3d96abfa9bd11cb22a25e1a")
	version("1.6.0", commit="ef9afdca79598f6b5e44939921cf15e7762f73cd")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biodb@1.3.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
