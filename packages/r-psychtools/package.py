# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsychtools(RPackage):
	"""Tools to Accompany the 'psych' Package for Psychological
Research

	Support functions,  data sets, and vignettes for the 'psych' package. Contains several of the biggest data sets for the 'psych' package as well as four vignettes. A few helper functions for file manipulation are included as well. For more information, see the <https://personality-project.org/r/> web page.
	"""
	
	homepage = "https://personality-project.org/r/psych/"
	cran = "psychTools" 

	version("2.4.3", md5="2787cfe0c035647c0d9c5a825f98ae0f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-rtf", type=("build", "run"))
