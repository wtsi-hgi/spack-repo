# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStressaddition(RPackage):
	"""Modelling Tri-Phasic Concentration-Response Relationships

	The stress addition approach is an alternative to the traditional
    concentration addition or effect addition models. It allows the modelling
    of tri-phasic concentration-response relationships either as single toxicant
    experiments, in combination with an environmental stressor or as mixtures of
    two toxicants. See Liess et al. (2019) <doi:10.1038/s41598-019-51645-4>
    and Liess et al. (2020) <doi:10.1186/s12302-020-00394-7>.
	"""
	
	homepage = "https://git.ufz.de/oekotox/stressaddition"
	cran = "stressaddition" 

	version("3.1.0", md5="27cb4fa771a0bc36486386ed9e5d6d3e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-drc@3:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
