# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmiccircos(RPackage):
	"""High-quality circular visualization of omics data

	OmicCircos is an R application and package for generating high-quality circular plots for omics data.
	"""
	
	bioc = "OmicCircos" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/OmicCircos_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/OmicCircos/OmicCircos_1.40.0.tar.gz"]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="2c21551a046ed6d5dd7bedb36eed4c3c664dbcfe39dee54266afae3c9db75fdb")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
