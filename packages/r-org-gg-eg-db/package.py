# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgGgEgDb(RPackage):
	"""Genome wide annotation for Chicken

	Genome wide annotation for Chicken, primarily based on mapping using Entrez Gene identifiers.
	"""
	
	bioc = "org.Gg.eg.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.Gg.eg.db_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.Gg.eg.db/org.Gg.eg.db_3.18.0.tar.gz"]

	version("3.18.0", sha256="cba7b6f3ac54250323c64dd50e9c6f7f2a27659de3ee7342b36143ef99ecb70c")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

