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

	version("1.62.0", md5="1a4887a4c08676e0ce69331caacc297e")

	depends_on("r@2.6.2:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-lpe", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
