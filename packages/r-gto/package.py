# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGto(RPackage):
	"""Insert 'gt' Tables into Word Documents

	Insert tables created by the 'gt' R package into 'Microsoft Word' 
    documents. This gives users the ability to add to their existing word documents
    the tables made in 'gt' using the familiar 'officer' package and syntax from
    the 'officeverse'.
	"""
	
	cran = "gto" 

	version("0.1.1", md5="7dc0de9e2a38324ced105812bd650d6e")

	depends_on("r-gt@0.8:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
