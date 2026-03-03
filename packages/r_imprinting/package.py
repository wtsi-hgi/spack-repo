# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImprinting(RPackage):
	"""Calculate Birth Year-Specific Probabilities of Immune Imprinting
to Influenza

	Reconstruct birth-year specific probabilities of immune imprinting to influenza A, using the methods of Gostic et al. (2016) <doi:10.1126/science.aag1322>. Plot, save, or export the calculated probabilities for use in your own research. By default, the package calculates subtype-specific imprinting probabilities, but with user-provided frequency data, it is possible to calculate probabilities for arbitrary kinds of primary exposure to influenza A, including primary vaccination and exposure to specific clades, strains, etc.
	"""
	
	homepage = "https://cobeylab.github.io/imprinting/"
	cran = "imprinting" 

	version("0.1.1", md5="eb2577811d6c14a76e14fad5cf9d5077")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-cowplot@1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
