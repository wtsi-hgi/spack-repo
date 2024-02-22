# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpaci(RPackage):
	"""Placido Analysis of Corneal Irregularity

	Analysis of corneal data obtained from a Placido disk corneal topographer with calculation of irregularity indices. This package performs analyses of corneal data obtained from a Placido disk corneal topographer, with the calculation of the Placido irregularity indices and the posterior analysis. The package is intended to be easy to use by a practitioner, providing a simple interface and yielding easily interpretable results. A corneal topographer is an ophthalmic clinical device that obtains measurements in the cornea (the anterior part of the eye). A Placido disk corneal topographer makes use of the Placido disk [Rowsey et al. (1981)]<doi:10.1001/archopht.1981.03930011093022>, which produce a circular pattern of measurement nodes. The raw information measured by such a topographer is used by practitioners to analyze curvatures, to study optical aberrations, or to diagnose specific conditions of the eye (e.g. keratoconus, an important corneal disease). The rPACI package allows the calculation of the corneal irregularity indices described in [Castro-Luna et al. (2020)]<doi:10.1016%2Fj.clae.2019.12.006>, [Ramos-Lopez et al. (2013)]<doi:10.1097%2FOPX.0b013e3182843f2a>, and [Ramos-Lopez et al. (2011)]<doi:10.1097/opx.0b013e3182279ff8>. It provides a simple interface to read corneal topography data files as exported by a typical Placido disk topographer, to compute the irregularity indices mentioned before, and to display summary plots that are easy to interpret for a clinician.
	"""
	
	homepage = "https://cran.r-project.org/package=rPACI"
	cran = "rPACI" 

	version("0.2.2", md5="7c6c8ee687cc47c33c5c4180017ab07a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
