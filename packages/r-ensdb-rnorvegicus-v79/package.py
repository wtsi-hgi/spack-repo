# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsdbRnorvegicusV79(RPackage):
	"""Ensembl based annotation package

	Exposes an annotation databases generated from Ensembl.
	"""
	
	bioc = "EnsDb.Rnorvegicus.v79" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EnsDb.Rnorvegicus.v79_2.99.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/EnsDb.Rnorvegicus.v79/EnsDb.Rnorvegicus.v79_2.99.0.tar.gz"]

	version("2.99.0", md5="7d305bd0d1a073bd8c60063ae210a7a9", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/EnsDb.Rnorvegicus.v79_2.99.0.tar.gz")
	version("2.99.0", md5="7d305bd0d1a073bd8c60063ae210a7a9", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EnsDb.Rnorvegicus.v79_2.99.0.tar.gz")

	depends_on("r-ensembldb", type=("build", "run"))

