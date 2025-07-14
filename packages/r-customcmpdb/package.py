# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCustomcmpdb(RPackage):
	"""Customize and Query Compound Annotation Database

	This package serves as a query interface for important community collections of small molecules, while also allowing users to include custom compound collections.
	"""
	
	homepage = "https://github.com/yduan004/customCMPdb/"
	bioc = "customCMPdb" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/customCMPdb_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/customCMPdb/customCMPdb_1.12.0.tar.gz"]

	version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="47f7d8b794bec9cc70004be50e6149210928cb58c408cffc321f805f3812b395")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-chemminer", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
