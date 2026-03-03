# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMft(RPackage):
	"""The Multiple Filter Test for Change Point Detection

	Provides statistical tests and algorithms for the detection of change points in time series and point processes - particularly for changes in the mean in time series and for changes in the rate and in the variance in point processes. References - Michael Messer, Marietta Kirchner, Julia Schiemann, Jochen Roeper, Ralph Neininger and Gaby Schneider (2014), A multiple filter test for the detection of rate changes in renewal processes with varying variance <doi:10.1214/14-AOAS782>. Stefan Albert, Michael Messer, Julia Schiemann, Jochen Roeper, Gaby Schneider (2017), Multi-scale detection of variance changes in renewal processes in the presence of rate change points <doi:10.1111/jtsa.12254>. Michael Messer, Kaue M. Costa, Jochen Roeper and Gaby Schneider (2017), Multi-scale detection of rate changes in spike trains with weak dependencies <doi:10.1007/s10827-016-0635-3>. Michael Messer, Stefan Albert and Gaby Schneider (2018), The multiple filter test for change point detection in time series <doi:10.1007/s00184-018-0672-1>. Michael Messer, Hendrik Backhaus, Albrecht Stroh and Gaby Schneider (2019+) Peak detection in time series.  
	"""
	
	cran = "MFT" 

	version("2.0", md5="a0090ef526ba2ffb988b20c5811f3b14")

