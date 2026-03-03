# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextgrid(RPackage):
	"""Praat TextGrid Objects in R

	The software application Praat can be used to annotate
    waveform data (e.g., to mark intervals of interest or to label events).
    (See <http://www.fon.hum.uva.nl/praat/> for more information about Praat.)
    These annotations are stored in a Praat TextGrid object, which consists of
    a number of interval tiers and point tiers. An interval tier consists of
    sequential (i.e., not overlapping) labeled intervals. A point tier consists
    of labeled events that have no duration. The 'textgRid' package provides
    S4 classes, generics, and methods for accessing information that is stored
    in Praat TextGrid objects.
	"""
	
	homepage = "www.praat.org"
	cran = "textgRid" 

	version("1.0.1", md5="219f1720368153e6379ee45ad29fa3c5")

	depends_on("r@3.2.3:", type=("build", "run"))
