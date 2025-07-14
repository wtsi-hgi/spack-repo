# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiotip(RPackage):
	"""BioTIP: An R package for characterization of Biological Tipping-Point

	Adopting tipping-point theory to transcriptome profiles to unravel disease regulatory trajectory.
	"""
	
	homepage = "https://github.com/xyang2uchicago/BioTIP"
	bioc = "BioTIP"

	version("1.22.0", commit="83de1273e39d8825a9fd44719ffc61d175098d4a")
	version("1.16.0", commit="910489bb12b68e14589da043708edfdbed9358af")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
