# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisualdom(RPackage):
	"""Visualize Dominant Variables in Wavelet Multiple Correlation

	Estimates and plots as a heat map the correlation coefficients obtained via the wavelet local multiple correlation 'WLMC' (Fernández-Macho 2018) and the 'dominant' variable/s, i.e., the variable/s that maximizes the multiple correlation through time and scale (Polanco-Martínez et al. 2020, Polanco-Martínez 2022). We improve the graphical outputs of WLMC proposing a didactic and useful way to visualize the 'dominant' variable(s) for a set of time series. The WLMC was designed for financial time series, but other kinds of data (e.g., climatic, ecological, etc.) can be used. The functions contained in 'VisualDom' are highly flexible since these contains several parameters to personalize the time series under analysis and the heat maps. In addition, we have also included two data sets (named 'rdata_climate' and 'rdata_Lorenz') to exemplify the use of the functions contained in 'VisualDom'. Methods derived from Fernández-Macho (2018) <doi:10.1016/j.physa.2017.11.050>, Polanco-Martínez et al. (2020) <doi:10.1038/s41598-020-77767-8> and Polanco-Martínez (2023, in press). 
	"""
	
	cran = "VisualDom" 

	version("0.8.0", md5="b889bf4119759bef013077ba9a08b419")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-waveslim", type=("build", "run"))
	depends_on("r-wavemulcor", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
