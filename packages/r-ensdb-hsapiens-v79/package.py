# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsdbHsapiensV79(RPackage):
	"""Ensembl based annotation package

	Exposes an annotation databases generated from Ensembl.
	"""
	
	bioc = "EnsDb.Hsapiens.v79" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EnsDb.Hsapiens.v79_2.99.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/EnsDb.Hsapiens.v79/EnsDb.Hsapiens.v79_2.99.0.tar.gz"]

	version("2.99.0", md5="16b5629805c07649b2aa501d34fcc588", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EnsDb.Hsapiens.v79_2.99.0.tar.gz")

	depends_on("r-ensembldb", type=("build", "run"))

	# annotation