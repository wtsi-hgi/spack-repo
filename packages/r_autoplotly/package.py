# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutoplotly(RPackage):
	"""Automatic Generation of Interactive Visualizations for
Statistical Results

	Functionalities to automatically generate interactive visualizations for
             statistical results supported by 'ggfortify', such as time series, PCA,
             clustering and survival analysis, with 'plotly.js' <https://plotly.com/>  and
             'ggplot2' style. The generated visualizations can also be easily extended
             using 'ggplot2' and 'plotly' syntax while staying interactive.
	"""
	
	homepage = "https://github.com/terrytangyuan/autoplotly"
	cran = "autoplotly" 

	version("0.1.4", md5="429b44007c4d2f46a6944b7bcf79067a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggfortify", type=("build", "run"))
