# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSylcount(RPackage):
	"""Syllable Counting and Readability Measurements

	An English language syllable counter, plus readability score
    measure-er. For readability, we support 'Flesch' Reading Ease and
    'Flesch-Kincaid' Grade Level ('Kincaid' 'et al'. 1975)
    <https://stars.library.ucf.edu/cgi/viewcontent.cgi?article=1055&context=istlibrary>,
    Automated Readability Index ('Senter' and Smith 1967)
    <https://apps.dtic.mil/sti/citations/AD0667273>,
    Simple Measure of Gobbledygook (McLaughlin 1969),
    and 'Coleman-Liau' (Coleman and 'Liau' 1975) <doi:10.1037/h0076540>. The
    package has been carefully optimized and should be very efficient, both in
    terms of run time performance and memory consumption. The main methods are
    'vectorized' by document, and scores for multiple documents are computed in
    parallel via 'OpenMP'.
	"""
	
	homepage = "https://github.com/wrathematics/sylcount"
	cran = "sylcount" 

	version("0.2-6", md5="3fe9dd311da7deb5bf95979108676891")

	depends_on("r@3:", type=("build", "run"))
