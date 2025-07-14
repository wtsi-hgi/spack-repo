# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMassir(RPackage):
	"""massiR: MicroArray Sample Sex Identifier

	Predicts the sex of samples in gene expression microarray datasets
	"""
	
	bioc = "massiR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/massiR_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/massiR/massiR_1.38.0.tar.gz"]

    version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="b43cb1cd4099fa7363a0bdd694077363255b6078d554f170274a55669b77609b")

	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-diptest", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r@3.0.2:", type=("build", "run"))
