# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdpf(RPackage):
	"""Use Least Squares Polynomial Regression and Statistical Testing
to Improve Savitzky-Golay

	This function takes a vector or matrix of data and smooths
    the data with an improved Savitzky Golay transform. The Savitzky-Golay
    method for data smoothing and differentiation calculates convolution
    weights using Gram polynomials that exactly reproduce the results of
    least-squares polynomial regression. Use of the Savitzky-Golay
    method requires specification of both filter length and
    polynomial degree to calculate convolution weights. For maximum
    smoothing of statistical noise in data, polynomials with
    low degrees are desirable, while a high polynomial degree
    is necessary for accurate reproduction of peaks in the data.
    Extension of the least-squares regression formalism with
    statistical testing of additional terms of polynomial degree
    to a heuristically chosen minimum for each data window leads
    to an adaptive-degree polynomial filter (ADPF). Based on noise
    reduction for data that consist of pure noise and on signal
    reproduction for data that is purely signal, ADPF performed
    nearly as well as the optimally chosen fixed-degree
    Savitzky-Golay filter and outperformed sub-optimally chosen
    Savitzky-Golay filters. For synthetic data consisting of noise
    and signal, ADPF outperformed both optimally chosen and
    sub-optimally chosen fixed-degree Savitzky-Golay filters. See Barak, P. (1995) <doi:10.1021/ac00113a006> for more information.
	"""
	
	cran = "ADPF" 

	version("0.0.1", md5="82badb8bbe3cbdc5099f8724f52ff3e9")

	depends_on("r@3.2.4:", type=("build", "run"))
