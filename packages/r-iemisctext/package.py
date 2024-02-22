# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIemisctext(RPackage):
	"""Irucka Embry's Miscellaneous Text Collection

	The eclectic collection includes the following written pieces:
    "The War Prayer" by Mark Twain, "War Is A Racket" by Major General
    Smedley Butler, "The Mask of Anarchy: Written on the Occasion of the
    Massacre at Manchester" by Percy Bysshe Shelley, "Connect the D.O.T.S." by
    Obiora Embry, "Untitled: Climate Strange" by Irucka Ajani Embry, and
    "Untitled: Us versus Them or People Screwing over Other People (as we all
    live on one Earth and there is no "us versus them" in the actual Ultimate
    Reality}" by Irucka Ajani Embry.
	"""
	
	homepage = "https://gitlab.com/iembry/iemisctext"
	cran = "iemisctext" 

	version("0.9.99", md5="07e3fcb3c7abd3f46c474e3614f00cf2")

	depends_on("r@3.1:", type=("build", "run"))
