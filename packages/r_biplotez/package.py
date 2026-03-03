# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiplotez(RPackage):
	"""EZ-to-Use Biplots

	Provides users with an EZ-to-use platform for representing data
             with biplots. Currently principal component analysis (PCA) and canonical variate
             analysis (CVA) biplots are included. This is accompanied by various formatting
             options for the samples and axes. Alpha-bags and concentration ellipses
             are included for visual enhancements and interpretation. For an extensive
             discussion on the topic, see Gower, J.C., Lubbe, S. and le Roux, N.J.
             (2011, ISBN: 978-0-470-01255-0) Understanding Biplots. Wiley: Chichester.
	"""
	
	cran = "biplotEZ" 

	version("1.2.0", md5="2d71925738aee73314636913b01da1af")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
