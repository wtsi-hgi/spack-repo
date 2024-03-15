# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodbmirbase(RPackage):
	"""biodbMirbase, a library for connecting to miRBase mature database

	The biodbMirbase library is an extension of the biodb framework package, that provides access to miRBase mature database. It allows to retrieve entries by their accession number, and run specific web services. Description: The biodbMirbase library provides access to the miRBase Database, using biodb package framework.
	"""
	
	bioc = "biodbMirbase" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/biodbMirbase_1.5.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/biodbMirbase/biodbMirbase_1.5.0.tar.gz"]

	version("1.5.0", md5="af331cadc2f7575e4dbf5345f19c61e6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biodb@1.3.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
