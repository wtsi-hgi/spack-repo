# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNorway981Db(RPackage):
	"""Norway981 http://genome-www5.stanford.edu/ Annotation Data (Norway981)

	Norway981 http://genome-www5.stanford.edu/ Annotation Data (Norway981) assembled using data from public repositories
	"""
	
	bioc = "Norway981.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Norway981.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/Norway981.db/Norway981.db_3.2.3.tar.gz"]

	version("3.2.3", md5="85367390919bba9018438585e59fbb87")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

