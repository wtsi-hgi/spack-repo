# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsdbMmusculusV79(RPackage):
	"""Ensembl based annotation package

	Exposes an annotation databases generated from Ensembl.
	"""
	
	bioc = "EnsDb.Mmusculus.v79" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EnsDb.Mmusculus.v79_2.99.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/EnsDb.Mmusculus.v79/EnsDb.Mmusculus.v79_2.99.0.tar.gz"]

	version("2.99.0", md5="28bbab743b0d2d550dbfa0bcd3274fad", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/EnsDb.Mmusculus.v79_2.99.0.tar.gz")
	version("2.99.0", md5="28bbab743b0d2d550dbfa0bcd3274fad", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EnsDb.Mmusculus.v79_2.99.0.tar.gz")

	depends_on("r-ensembldb", type=("build", "run"))

