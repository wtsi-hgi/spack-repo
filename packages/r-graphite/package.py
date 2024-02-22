# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphite(RPackage):
	"""GRAPH Interaction from pathway Topological Environment

	Graph objects from pathway topology derived from KEGG, Panther, PathBank, PharmGKB, Reactome SMPDB and WikiPathways databases.
	"""
	
	homepage = "https://github.com/sales-lab/graphite"
	bioc = "graphite" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/graphite_1.48.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/graphite/graphite_1.48.0.tar.gz"]

	version("1.48.0", md5="532e304cdb96a828c4b764bfd36cce85")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-graph@1.67.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
