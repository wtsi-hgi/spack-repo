# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRglCry(RPackage):
	"""'cry' and 'rgl' — Applications in Crystallography

	Visualizing crystal structures and selected area electron diffraction (SAED) patterns.  It provides functions cry_demo() and dp_demo() to load a file in 'CIF' (Crystallographic Information Framework) formats and display crystal structures and electron diffraction patterns.  The function dp_demo() also performs simple simulation of powder X-ray diffraction (PXRD) patterns, and the results can be saved to a file in the working directory.  The package has been tested on several platforms, including Linux on 'Crostini' with a Core™ m3-8100Y Chromebook, I found that even on this low-powered platform, the performance was acceptable.
    T. Hanashima (2001) <https://www2.kek.jp/imss/pf/tools/sasaki/sinram/sinram.html>
    Todd Helmenstine (2019) <https://sciencenotes.org/molecule-atom-colors-cpk-colors/>
    Wikipedia contributors (2023) <https://en.wikipedia.org/w/index.php?title=Atomic_radius&oldid=1179864711>.
	"""
	
	homepage = "https://github.com/SaitouToshihide/rgl.cry/"
	cran = "rgl.cry" 

	version("0.1.0", md5="44cfb07fc4e2f3e5de7730f6d7a32160")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cry", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
