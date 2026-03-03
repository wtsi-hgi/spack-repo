# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmpeaksr(RPackage):
	"""Conducting the Peak Fitting Based on the EM Algorithm

	The peak fitting of spectral data is performed by using the frame work of EM algorithm. We adapted the EM algorithm for the peak fitting of spectral data set by considering the weight of the intensity corresponding to the measurement energy steps    (Matsumura, T., Nagamura, N., Akaho, S., Nagata, K., & Ando, Y. (2019, 2021 and 2023) <doi:10.1080/14686996.2019.1620123>, <doi:10.1080/27660400.2021.1899449> <doi:10.1080/27660400.2022.2159753>. The package efficiently estimates the parameters of Gaussian mixture model during iterative calculation between E-step and M-step, and the parameters are converged to a local optimal solution. This package can support the investigation of peak shift with two advantages: (1) a large amount of data can be processed at high speed; and (2) stable and automatic calculation can be easily performed.
	"""
	
	cran = "EMpeaksR" 

	version("0.3.1", md5="467acbe0465c2faa0b9e1a013ec0ecef")

