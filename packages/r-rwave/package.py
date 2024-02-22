# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwave(RPackage):
	"""Time-Frequency Analysis of 1-D Signals

	A set of R functions which provide an
        environment for the Time-Frequency analysis of 1-D signals (and
        especially for the wavelet and Gabor transforms of noisy
        signals). It was originally written for Splus by Rene Carmona,
        Bruno Torresani, and Wen L. Hwang, first at the University of
        California at Irvine and then at Princeton University.  Credit
        should also be given to Andrea Wang whose functions on the
        dyadic wavelet transform are included. Rwave is based on the
        book: "Practical Time-Frequency Analysis: Gabor and Wavelet
        Transforms with an Implementation in S", by Rene Carmona, Wen
        L. Hwang and Bruno Torresani (1998, eBook ISBN:978008053942), Academic Press.
	"""
	
	homepage = "https://carmona.princeton.edu/TFbook/tfbook.html"
	cran = "Rwave" 

	version("2.6-5", md5="27fa1790348a2d01955b5636bc9cf060")

	depends_on("r@2.14:", type=("build", "run"))
