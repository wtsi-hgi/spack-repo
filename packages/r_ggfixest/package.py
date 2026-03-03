# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgfixest(RPackage):
	"""Dedicated 'ggplot2' Methods for 'fixest' Objects

	Provides 'ggplot2' equivalents of fixest::coefplot() and fixest::iplot(),
    for producing nice coefficient plots and interaction plots. Enables some
    additional functionality and convenience features, including grouped
    multi-'fixest' object faceting and programmatic updates to existing plots
    (e.g., themes and aesthetics).
	"""
	
	homepage = "http://grantmcdermott.com/ggfixest/"
	cran = "ggfixest" 

	version("0.1.0", md5="18dad06d086b00d4bbd16f0d8a2296eb")

	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-fixest@0.11.2:", type=("build", "run"))
	depends_on("r-dreamerr", type=("build", "run"))
	depends_on("r-ggh4x", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-marginaleffects@0.10:", type=("build", "run"))
