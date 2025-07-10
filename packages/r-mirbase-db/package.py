# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirbaseDb(RPackage):
	"""miRBase: the microRNA database

	miRBase: the microRNA database assembled using data from miRBase (http://www.mirbase.org/).
	"""
	
	bioc = "mirbase.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mirbase.db_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mirbase.db/mirbase.db_1.2.0.tar.gz"]

	version("1.2.0", sha256="b335df59433f2ad0e61938d3563e0106e48b6d52386cb1950930e0a36280ea50")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

