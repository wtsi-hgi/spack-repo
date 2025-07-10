# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirbaseversionsDb(RPackage):
	"""Collection of mature miRNA names of 22 different miRBase release versions

	Annotation package containing all available miRNA names from 22 versions (data from http://www.mirbase.org/).
	"""
	
	bioc = "miRBaseVersions.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/miRBaseVersions.db_1.1.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/miRBaseVersions.db/miRBaseVersions.db_1.1.0.tar.gz"]

	version("1.1.0", sha256="1cc65f746c705d061aa6f5172563389d5abe412dd446c5cd1b456afa1218c026")

	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))

