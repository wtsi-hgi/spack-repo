# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlpe(RPackage):
	"""Local Pooled Error Test for Differential Expression with Paired High-throughput Data

	This package performs tests for paired high-throughput data.
	"""
	
	homepage = "http://www.korea.ac.kr/~stat2242/"
	bioc = "PLPE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PLPE_1.62.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PLPE/PLPE_1.62.0.tar.gz"]

	version("1.68.0", tag="RELEASE_3_21")
	version("1.62.0", sha256="614f11be46858c8269ede6ccc5f5db513e78fb13d43ccbfef4008e43b932f079")

	depends_on("r@2.6.2:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-lpe", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
