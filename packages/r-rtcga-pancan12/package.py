# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcgaPancan12(RPackage):
	"""PanCan 12 from Genome Cancer Browser

	Package provides clinical, expression, cnv and mutation data from Genome Cancer Browser.
	"""
	
	bioc = "RTCGA.PANCAN12" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RTCGA.PANCAN12_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RTCGA.PANCAN12/RTCGA.PANCAN12_1.30.0.tar.gz"]

	version("1.30.0", sha256="b4ed9beac6574fcd6976f3fcf55c2a4ae8c1128fbe0396b58aba827ad713e7c7", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RTCGA.PANCAN12_1.30.0.tar.gz")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rtcga", type=("build", "run"))

