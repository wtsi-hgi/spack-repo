# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImageTextlinedetector(RPackage):
	"""Segment Images in Text Lines and Words

	Find text lines in scanned images and segment the lines into words.
    Includes implementations of the paper 'Novel A* Path Planning Algorithm for Line Segmentation of Handwritten Documents' by Surinta O. et al (2014) <doi:10.1109/ICFHR.2014.37> available at <https://github.com/smeucci/LineSegm>,
    an implementation of 'A Statistical approach to line segmentation in handwritten documents' by Arivazhagan M. et al (2007) <doi:10.1117/12.704538>, 
    and a wrapper for an image segmentation technique to detect words in text lines as described in the paper 'Scale Space Technique for Word Segmentation in Handwritten Documents' by Manmatha R. and Srimal N. (1999) paper at <doi:10.1007/3-540-48236-9_3>, wrapper for code available at <https://github.com/arthurflor23/text-segmentation>.
    Provides as well functionality to put cursive text in images upright using the approach defined in the paper 'A new normalization technique for cursive handwritten words' by  Vinciarelli A. and Luettin J. (2001) <doi:10.1016/S0167-8655(01)00042-3>. 
	"""
	
	homepage = "https://github.com/DIGI-VUB/image.textlinedetector"
	cran = "image.textlinedetector" 

	version("0.2.3", md5="4176d6ec469750525404303e44c8c1d4")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
