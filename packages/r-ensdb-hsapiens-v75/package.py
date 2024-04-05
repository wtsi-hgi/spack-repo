# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsdbHsapiensV75(RPackage):
	"""Ensembl based annotation package

	Exposes an annotation databases generated from Ensembl.
	"""
	
	bioc = "EnsDb.Hsapiens.v75" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EnsDb.Hsapiens.v75_2.99.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/EnsDb.Hsapiens.v75/EnsDb.Hsapiens.v75_2.99.0.tar.gz"]

	version("2.99.0", md5="6c896475252903972bfc6c0eb0d8f334", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/EnsDb.Hsapiens.v75_2.99.0.tar.gz")
	version("2.99.0", md5="6c896475252903972bfc6c0eb0d8f334", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EnsDb.Hsapiens.v75_2.99.0.tar.gz")

	depends_on("r-ensembldb", type=("build", "run"))

