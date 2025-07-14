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

	version("1.38.0", commit="4fa6dd2a3d4fea971a55e3887127654327499272")
	version("1.32.0", commit="2992eacba644c84e35b824d22d18fc6f5186d6f6")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
