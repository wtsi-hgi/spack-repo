# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemand(RPackage):
	"""DeMAND

	DEMAND predicts Drug MoA by interrogating a cell context specific regulatory network with a small number (N >= 6) of compound-induced gene expression signatures, to elucidate specific proteins whose interactions in the network is dysregulated by the compound.
	"""
	
	bioc = "DeMAND" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DeMAND_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DeMAND/DeMAND_1.32.0.tar.gz"]

	version("1.32.0", md5="ccb354bddebbebda6c42453810f10e70")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
