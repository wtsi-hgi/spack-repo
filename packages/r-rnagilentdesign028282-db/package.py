# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnagilentdesign028282Db(RPackage):
	"""Agilent Chips that use Agilent design number 028282 annotation data (chip RnAgilentDesign028282)

	Agilent Chips that use Agilent design number 028282 annotation data (chip RnAgilentDesign028282) assembled using data from public repositories
	"""
	
	bioc = "RnAgilentDesign028282.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/RnAgilentDesign028282.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/RnAgilentDesign028282.db/RnAgilentDesign028282.db_3.2.3.tar.gz"]

	version("3.2.3", md5="72cafb0f7514a81f462acb3248e21aa9")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.3:", type=("build", "run"))

	# annotation