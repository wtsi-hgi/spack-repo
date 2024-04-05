# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReactomeDb(RPackage):
	"""A set of annotation maps for reactome

	A set of annotation maps for reactome assembled using data from reactome. This package has been created by a third-party developer, and is not affiliated with the Reactome team.
	"""
	
	bioc = "reactome.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/reactome.db_1.86.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/reactome.db/reactome.db_1.86.2.tar.gz"]

	version("1.86.2", md5="ff56f3908b347cb18e3e4ccedf7f584e")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

