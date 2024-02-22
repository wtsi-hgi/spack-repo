# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrassp(RPackage):
	"""Interface to the 'ASSP' Library

	A wrapper around Michel Scheffers's 'libassp' (<https://libassp.sourceforge.net/>).
    The 'libassp' (Advanced Speech Signal Processor) library aims at providing
    functionality for handling speech signal files in most common audio formats
    and for performing analyses common in phonetic science/speech science. This
    includes the calculation of formants, fundamental frequency, root mean
    square, auto correlation, a variety of spectral analyses, zero crossing
    rate, filtering etc. This wrapper provides R with a large subset of
    'libassp's signal processing functions and provides them to the user in a
    (hopefully) user-friendly manner.
	"""
	
	homepage = "https://github.com/IPS-LMU/wrassp"
	cran = "wrassp" 

	version("1.0.5", md5="032717084a657539684aadf963f5b595")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-tibble@2.1:", type=("build", "run"))
