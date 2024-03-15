# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnimation(RPackage):
	"""A Gallery of Animations in Statistics and Utilities to Create
	Animations.

	Provides functions for animations in statistics, covering topics in
	probability theory, mathematical statistics, multivariate statistics,
	non-parametric statistics, sampling survey, linear models, time series,
	computational statistics, data mining and machine learning.  These
	functions maybe helpful in teaching statistics and data analysis."""

	cran = "animation"

	license("GPL-2.0-or-later")

	version("2.7", md5="57e4bbd7c116ac0e6077eb613aa5ecf4")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("imagemagick", type=("build", "link", "run"))
	depends_on("ffmpeg", type=("build", "link", "run"))
