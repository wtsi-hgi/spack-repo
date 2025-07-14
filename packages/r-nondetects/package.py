# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNondetects(RPackage):
	"""Non-detects in qPCR data

	Methods to model and impute non-detects in the results of qPCR experiments.
	"""
	
	bioc = "nondetects" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/nondetects_2.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/nondetects/nondetects_2.32.0.tar.gz"]

	version("2.38.1", tag="RELEASE_3_21")
	version("2.32.0", sha256="9b99b3c3226cea1f16ea6574ed9b9df4b0a31c258f9b0a73ba7fed75cbab020c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biobase@2.22:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-htqpcr@1.16:", type=("build", "run"))
