# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBannercommenter(RPackage):
	"""Make Banner Comments with a Consistent Format

	A convenience package for use while drafting code.
    It facilitates making stand-out comment lines decorated with
    bands of characters.  The input text strings are converted into
    R comment lines, suitably formatted. These are then displayed in
    a console window and, if possible, automatically transferred to a
    clipboard ready for pasting into an R script.  Designed to save
    time when drafting R scripts that will need to be navigated and
    maintained by other programmers.
	"""
	
	cran = "bannerCommenter" 

	version("1.0.0", md5="2dac5b37024ceee80562a2086d32b2b8")

