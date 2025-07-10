# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrosgenome1cdf(RPackage):
	"""drosgenome1cdf

	A package containing an environment representing the DrosGenome1.CDF file.
	"""
	
	bioc = "drosgenome1cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/drosgenome1cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/drosgenome1cdf/drosgenome1cdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="3ebc8e1e2820c1a9ad09cd4ece7b91469ae1297335cb597e53a37bf52d9ba60b")

	depends_on("r-annotationdbi", type=("build", "run"))

