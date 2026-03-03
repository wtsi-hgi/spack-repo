# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmagilentdesign026655Db(RPackage):
	"""Agilent Chips that use Agilent design number 026655 annotation data (chip MmAgilentDesign026655)

	Agilent Chips that use Agilent design number 026655 annotation data (chip MmAgilentDesign026655) assembled using data from public repositories
	"""
	
	bioc = "MmAgilentDesign026655.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/MmAgilentDesign026655.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/MmAgilentDesign026655.db/MmAgilentDesign026655.db_3.2.3.tar.gz"]

	version("3.2.3", md5="7ef619bd2c74f22ea4f3c2b2c4131fe9")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.3:", type=("build", "run"))

