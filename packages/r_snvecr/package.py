# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnvecr(RPackage):
	"""Calculate Earth’s Obliquity and Precession in the Past

	Easily calculate precession and obliquity from an orbital solution (defaults to ZB18a from Zeebe and Lourens (2019) <doi:10.1126/science.aax0612>) and assumed or reconstructed values for tidal dissipation (Td) and dynamical ellipticity (Ed). This is a translation and adaptation of the C-code in the supplementary material to Zeebe and Lourens (2022) <doi:10.1029/2021PA004349>, with further details on the methodology described in Zeebe (2022) <doi:10.3847/1538-3881/ac80f8>. The name of the C-routine is snvec, which refers to the key units of computation: spin vector s and orbit normal vector n.
	"""
	
	homepage = "https://japhir.github.io/snvecR/"
	cran = "snvecR" 

	version("3.9.1", md5="8f32641d5740436d368b1250ca486528")
	version("3.8.0", md5="79b994f1099743a62cf77e12d25ad390")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-cli@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
