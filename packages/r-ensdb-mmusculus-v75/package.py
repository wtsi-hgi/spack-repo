# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsdbMmusculusV75(RPackage):
	"""Ensembl based annotation package

	Exposes an annotation databases generated from Ensembl.
	"""
	
	bioc = "EnsDb.Mmusculus.v75" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/EnsDb.Mmusculus.v75_2.99.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/EnsDb.Mmusculus.v75/EnsDb.Mmusculus.v75_2.99.0.tar.gz"]

	version("2.99.0", md5="081bf6f90ff77031b634b4fe32e00be8", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/EnsDb.Mmusculus.v75_2.99.0.tar.gz")

	depends_on("r-ensembldb", type=("build", "run"))

	# annotation